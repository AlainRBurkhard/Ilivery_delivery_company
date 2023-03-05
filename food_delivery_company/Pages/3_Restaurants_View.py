#==============\importing libraries ==============#

import pandas as pd
import io
import plotly.express as px
import folium
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
from haversine import haversine
import plotly.graph_objects as go
import numpy as np

st.set_page_config( page_title= 'Restaurants View', page_icon = '🍛', layout = 'wide')

daf=pd.read_csv('dataset/train.csv')
df = daf.copy()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions import clean_df

df = clean_df(df)

## ------------------------------------------------##
#                   STREAMLIT
## ------------------------------------------------##

from functions import sidebar

df = sidebar(df)  

##==================================================##
#                   Layout Streamlit
##==================================================##
with st.container():
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        #avg distance between deliver and restaurant
        cols = ['Delivery_location_latitude', 'Delivery_location_longitude', 'Restaurant_latitude', 'Restaurant_longitude']
        df['distance'] = df.loc[:,cols].apply( lambda x:
                                      haversine( (x['Restaurant_latitude'], x['Restaurant_longitude']),
                                                (x['Delivery_location_latitude'],
                                                    x['Delivery_location_longitude']) ), axis=1)
        avg_distance = np.round(df['distance'].mean(),2)
        col1.metric(label = 'Avg. Delivery Distance (KM) ',value = avg_distance, delta = None)
    
    with col2:
        #avg time taken by delivery during no festival time
        df_aux = (df.loc[:, ['Time_taken(min)', 'Festival']]
                .groupby('Festival')
                  .agg( {'Time_taken(min)' :['mean', 'std']}))
        df_aux.columns = ['avg_time', 'std_time']
        df_aux = df_aux.reset_index()
        df_aux = np.round(df_aux.loc[df_aux['Festival'] == 'No ','avg_time'],2)
        col2.metric(label = 'Avg. Time (min)',value = df_aux, delta = None)    
    
    with col3:
        #avg time taken by delivery during festival time
        df_aux = (df.loc[:, ['Time_taken(min)', 'Festival']]
                .groupby('Festival')
                  .agg( {'Time_taken(min)' :['mean', 'std']}))
        df_aux.columns = ['avg_time', 'std_time']
        df_aux = df_aux.reset_index()
        df_aux = np.round(df_aux.loc[df_aux['Festival'] == 'Yes ','avg_time'],2) 
        col3.metric(label = 'Avg. Time During Festival (min)',value = df_aux, delta = None)

with st.container():
    st.markdown("""---""")
    col1 , col2 = st.columns(2, gap="large")
    with col1:
        #avg time by delivey per city and traffic
        st.subheader("Time Taken per Traffic")
        cols = ['City', 'Time_taken(min)', 'Road_traffic_density']
        df_aux = df.loc[:, cols].groupby(['City','Road_traffic_density']).agg( {'Time_taken(min)' :['mean', 'std']})
        df_aux.columns = ['avg_time', 'std_time']
        df_aux = df_aux.reset_index()

        st.plotly_chart(px.sunburst(df_aux, path=['City', 'Road_traffic_density'], values='avg_time',
                      color='std_time', color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df_aux['std_time'])), use_container_width=True)
    with col2:
        st.subheader("Avg. Time of Delivery by City")
        #avg and std time of delivery
        cols = ['City', 'Time_taken(min)']
        df_aux = df.loc[:, cols].groupby('City').agg( {'Time_taken(min)' :['mean', 'std']})
        df_aux.columns = ['avg_time', 'std_time']
        df_aux = df_aux.reset_index()
        fig = go.Figure()
        fig.add_trace ( go.Bar (name= 'Control',
                            x=df_aux['City'],
                            y=df_aux['avg_time'],
                            error_y=dict(type='data', array=df_aux['std_time'])))
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.subheader("Type of Order")
        typeoforder = df.groupby('Type_of_order')['ID'].count().reset_index()
        st.plotly_chart(px.pie(typeoforder, values='ID', names='Type_of_order'), use_container_width=True)
    with col2:
        st.subheader("Localization of Restaurants")
        restaurants = df.groupby('City')['ID'].count().reset_index()
        st.plotly_chart(px.pie(restaurants, values='ID', names='City'), use_container_width=True)
        