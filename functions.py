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
#====================== Functions ============================#

def cl_df(df):
    """ 
    Function responsable for cleaning the dataframe
    1.delete empty cells on the dataframe 'NaN
    2.deleting empty spaces in object type cells with strip
    3.change variables types
    
    Input: Dataframe
    Output: Dataframe
    """

    # cleaning empty cells#

    df = df[~df.isin(['NaN ']).any(axis=1)].reset_index(drop=True)

    # deleting space#
    df['ID'] = df['ID'].apply(str.strip)
    df['Delivery_person_ID'] = df['Delivery_person_ID'].apply(str.strip)
    df['Road_traffic_density'] = df['Road_traffic_density'].apply(str.strip)
    df['Weatherconditions'] = df['Weatherconditions'].apply(str.strip)
    
    mask = df['Weatherconditions'].str.contains('conditions')
    # use str.replace() to remove the string 'conditions' from the 'Description' column
    df.loc[mask, 'Weatherconditions'] = df.loc[mask, 'Weatherconditions'].str.replace('conditions', '')

    cols =['Weatherconditions','Road_traffic_density','Type_of_order','Type_of_vehicle','City']
    df[cols] = df[cols].apply(lambda x: x.str.strip())

    # transforming variables #
    df['Delivery_person_Age'] = df['Delivery_person_Age'].astype(int)
    df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].astype(float)
    df['Order_Date'] = pd.to_datetime( df['Order_Date'], format='%d-%m-%Y' )
    df['multiple_deliveries'] = df['multiple_deliveries'].astype( int )
    df['Time_taken(min)'] = df['Time_taken(min)'].apply(lambda x: x.split( '(min) ')[1])
    df['Time_taken(min)'] = df['Time_taken(min)'].astype(int)

    df.reset_index(inplace=True)
    df.index.astype(int)

    return df

def sidebar(df):
    
    
    st.sidebar.markdown('# iLivery')
    st.sidebar.markdown('## Fast Home Food')
    st.sidebar.markdown("""---""")

    date_slider = st.sidebar.slider(
        'Date',
        value=pd.Timestamp('2022-04-13'),
        min_value=pd.Timestamp('2022-02-11'),
        max_value=pd.Timestamp('2022-04-06'),    
        format='YYYY-MM-DD'
    )

    st.sidebar.markdown("""---""")

    ## ---- Traffic filter ----##

    traffic_conditions = st.sidebar.multiselect(
        'Traffic density',
        ['Low', 'Medium', 'High', 'Jam'],
        default=['Low', 'Medium', 'High', 'Jam'])

    st.sidebar.markdown("""---""")

    ## ---- Weather filter ----##

    Weatherconditions_filter = st.sidebar.multiselect(
        'Weathercondition',
        ['Sunny', 'Stormy', 'Cloudy', 'Sandstorms', 'Windy','Fog'],
        default=['Sunny', 'Stormy', 'Cloudy', 'Sandstorms', 'Windy','Fog'])

    st.sidebar.markdown("""---""")
    st.sidebar.markdown('#### Powered by Ramon Burkhard')

    #---------setting the filters-------------#
    
    # Date filter
    selected_lines = df['Order_Date'] < date_slider
    df = df.loc[selected_lines, :]

    #traffic filter
    selected_lines = df['Road_traffic_density'].isin(traffic_conditions)
    df = df.loc[selected_lines,:]

    # #weathercondition filter
    selected_lines = df['Weatherconditions'].isin(Weatherconditions_filter)
    df = df.loc[selected_lines,:]
    
    return df
