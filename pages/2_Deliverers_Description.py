#==============\importing libraries ==============#

import pandas as pd
import io
import plotly.express as px
import folium
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_folium import folium_static

st.set_page_config( page_title= 'Deliverers Description', page_icon = '🚛', layout = 'wide')

daf=pd.read_csv('dataset/train.csv')
df = daf.copy()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions import cl_df

df = cl_df(df)

## ------------------------------------------------##
#                   STREAMLIT
## ------------------------------------------------##

from functions import sidebar

df = sidebar(df)

##==================================================##
#                   Layout        
##==================================================##


with st.container():
    st.subheader("Deliver's Metric")
    col1, col2, col3, col4= st.columns([1,1,1,2])
    with col1:
        delivery_unique = len(df.loc[:, 'Delivery_person_ID'].unique())
        col1.metric(label='Deliverers',value = delivery_unique, delta = None)
    with col2:
        oldest = df['Delivery_person_Age'].max()
        st.metric(label='Older Deliverer',value = oldest, delta = None)
    with col3:
        youngster =df['Delivery_person_Age'].min()
        st.metric(label='Younger Deliverer',value = youngster, delta = None)
    with col4:
        grouped = df.groupby('City')
        median = grouped['Delivery_person_Age'].mean().round(2).reset_index(inplace=False)
        st.dataframe(median)
    
with st.container():
    st.markdown("""----""")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("Deliver's Ratings")
        dx= (df.loc[:,['Delivery_person_ID','Delivery_person_Ratings']]
            .groupby('Delivery_person_ID')
            .mean()
            .round(2)
            .reset_index())
        dx = dx.sort_values(by='Delivery_person_Ratings', ascending=False)
        st.dataframe(dx)
    with col2:
        st.subheader("Ratings by Traffic Density")
        m_traffic = df.groupby('Road_traffic_density')['Delivery_person_Ratings'].mean().reset_index()
        st.plotly_chart(px.bar(m_traffic, x='Road_traffic_density', y='Delivery_person_Ratings'), use_container_width=True)
        
with st.container():
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("Ratings by Weatherconditions")
        weather_ratings = df.groupby('Weatherconditions')['Delivery_person_Ratings'].mean().reset_index()
        st.plotly_chart(px.bar(weather_ratings, x='Weatherconditions', y='Delivery_person_Ratings'), use_container_width=True)
    with col2:
        st.subheader("Type of Vehicles")
        vehicles = df.groupby('Type_of_vehicle')['ID'].count().reset_index()
        st.plotly_chart(px.pie(vehicles, values='ID', names='Type_of_vehicle'), use_container_width=True)
        
with st.container():
    col1, col2 = st.columns(2, gap="large")
    with col1:
        dy = df.loc[:,['Delivery_person_ID','Time_taken(min)']]
        dy = dy.groupby('Delivery_person_ID').min().reset_index().sort_values('Time_taken(min)').head(10)
        st.subheader("Fastest Deliverer")
        st.dataframe(dy)
    with col2:
        dz = df.loc[:,['Delivery_person_ID','Time_taken(min)']]
        dz = dz.groupby('Delivery_person_ID').max().reset_index().sort_values('Time_taken(min)').head(10)
        st.subheader("Slowest Deliverer")
        st.dataframe(dz)
