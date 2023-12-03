import pandas as pd
import plotly.express as px
import streamlit as st
import os
from dotenv import load_dotenv

data_list = [
    {
        'business_id': 'Pns2l4eNsfO8kk83dixA6A',
        'name': 'Abby Rappoport, LAC, CMQ',
        'address': '1616 Chapala St, Ste 2',
        'city': 'Santa Barbara',
        'state': 'CA',
        'postal_code': '93101',
        'latitude': 34.4266787,
        'longitude': -119.7111968,
        'business_stars': 5.0,
        'review_count': 7,
        'is_open': 1,
        'categories': ['Retail']
    },
    {
        'business_id': 'IDtLPgUrqorrpqSLdfMhZQ',
        'name': 'Helena Avenue Bakery',
        'address': '456 Oak St',
        'city': 'Santa Barbara',
        'state': 'CA',
        'postal_code': '93101',
        'latitude': 34.4144445,
        'longitude': -119.6906718,
        'business_stars': 4.0,
        'review_count': 38,
        'is_open': 1,
        'categories': ['Food', 'Restaurant']
    },
    {
        'business_id': 'bYjnX_J1bHZob10DoSFkqQ',
        'name': '805 Ink',
        'address': '1228 State St',
        'city': 'Santa Barbara',
        'state': 'CA',
        'postal_code': '93101',
        'latitude': 34.4241297,
        'longitude': -119.7053211,
        'business_stars': 4.2,
        'review_count': 120,
        'is_open': 1,
        'categories': ['Food', 'Bakery']
    },
    {
        'business_id': '25Uww0C0wvF9CZ_3B6vWtA',
        'name': 'Enjoy The Mountain',
        'address': '1 Garden St',
        'city': 'Santa Barbara',
        'state': 'CA',
        'postal_code': '93105',
        'latitude': 34.4143420056,
        'longitude': -119.6873324599,
        'business_stars': 3.8,
        'review_count': 90,
        'is_open': 0,
        'categories': ['Retail', 'Shopping']
    },
        {
        'business_id': 'xF9r1XbMvEOsJeHlmFhIvw',
        'name': 'Weddings in Santa Barbara',
        'address': '263 Santa Monica Way',
        'city': 'Santa Barbara',
        'state': 'CA',
        'postal_code': '93109',
        'latitude': 34.3982982,
        'longitude': -119.725931,
        'business_stars': 4.2,
        'review_count': 120,
        'is_open': 1,
        'categories': ['Retail', 'Shopping']
    }   
]

restaurants = pd.DataFrame(data_list)


#st.title("Restaurants Map")

load_dotenv()

MAPBOX_TOKEN = os.environ["MAPBOX_TOKEN"]

#px.set_mapbox_access_token(open(".mapbox_token").read())
px.set_mapbox_access_token(MAPBOX_TOKEN)
fig = px.scatter_mapbox(restaurants,
                        lon = 'longitude',
                        lat = 'latitude',
                        hover_name = 'name',
                        hover_data = ['address', 'city', 'business_stars', 'review_count'],
                        color_discrete_sequence=['rgba(0,0,255, 1)'], 
                        size = 'review_count',
                        size_max = 15,
                        zoom = 10,
                        title = 'Interactive Map'
)

