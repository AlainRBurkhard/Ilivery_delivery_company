#=============== importing libraries ==============#

import pandas as pd
import io
import plotly as plot
import plotly.express as px
import folium
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_folium import folium_static

st.set_page_config( page_title= 'Strategy Panorama', page_icon = '📈', layout = 'wide')
                   
daf=pd.read_csv('dataset/train.csv')
df = daf.copy()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

  

## ------------------------------------------------##
#                   STREAMLIT
## ------------------------------------------------##

from functions import sidebar

df = sidebar(df)

##==================================================##
#                   Layout 
##==================================================##

tab1, tab2, tab3 = st.tabs( ['Comercial' , 'Strategy', 'Map'])

with tab1:
    with st.container():
        #orders per day
        st.header('Orders per Day')
        order_day = df.groupby('Order_Date').count().reset_index()
        st.plotly_chart(px.bar(order_day, x='Order_Date' , y='ID'), use_container_width=True)
    with st.container():
        col1, col2 = st.columns(2,gap="large")
        with col1:
            #Quantity of orders per city and density
            st.header('Orders per City and Density')
            city_road_df = df.loc[:,['ID','City','Road_traffic_density']].groupby(['Road_traffic_density','City']).count().reset_index()
            st.plotly_chart(px.scatter(city_road_df, x='City', y= 'Road_traffic_density', size = 'ID'), use_container_width=True)
        with col2:
            #orders per weathercondition
            st.header('Orders per Weathercondition')
            traf_order = df.groupby('Weatherconditions').count().reset_index()
            st.plotly_chart(px.pie(traf_order, values='ID', names='Weatherconditions'), use_container_width=True)
    
with tab2:
        with st.container():
            #orders per week
            st.header('Orders per Week')
            df['week_of_year'] = df['Order_Date'].dt.strftime( "%U" )
            df_week = df.groupby('week_of_year').count().reset_index()
            st.plotly_chart(px.bar(df_week, x='week_of_year' , y='index'), use_container_width=True)

        with st.container():    
            #Weekly orders mean by delivery person
            st.header('Average Weekly Orders per Deliverer')
            df_aux = df.loc[:, ['ID', 'Delivery_person_ID', 'week_of_year']].groupby('week_of_year').agg({'ID': 'count', 'Delivery_person_ID': 'nunique'}).reset_index()
            df_aux['order_by_delivery'] = df_aux['ID'] / df_aux['Delivery_person_ID']
            st.plotly_chart(px.line( df_aux, x='week_of_year', y='order_by_delivery' ), use_container_width=True)
                       
with tab3:
    with st.container():
        # geo center of deliveries
        st.header('Deliveries Geo Center')
        cols=['Road_traffic_density','City','Delivery_location_latitude','Delivery_location_longitude']
        ct = df.loc[:, cols].groupby(['Road_traffic_density','City']).median().reset_index()

        map1=folium.Map(zoom_start=100,control_scale=True)
        for index, location_info in ct.iterrows():
                folium.Marker([location_info['Delivery_location_latitude'],location_info['Delivery_location_longitude']],popup=location_info['City'] + ' ' + '$' + str(location_info['Road_traffic_density'])).add_to(map1)

        map1.fit_bounds(map1.get_bounds(), padding=(40, 40))
        folium_static(map1, width=800, height=400)
