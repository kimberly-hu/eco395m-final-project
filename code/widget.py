import streamlit as st
import pandas as pd
import plotly.express as px
from match import match


# This is used for testing. DELETE LATER.
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

# Use this for actual project.
# data_list = match()


zipcode = st.number_input("Insert your zipcode", min_value=0, step=1, format="%i")
st.write('The current zipcode is ', zipcode)

# Used for testing.
def recommendation():
    user_query = st.session_state.name
    matching_results = match(user_query, zipcode)
    if matching_results:
        for result in matching_results:
            st.write(result)  
    else:
        st.write("No matching results found.")

# def recommendation():
#     user_query = st.session_state.name
#     matching_results = match(user_query, zipcode)
#     if matching_results:
#         for result in matching_results:
#             st.write(result)  
#     else:
#         st.write("No matching results found.")

with st.form(key="my_form"):
    st.text_input("Any thoughts on where to eat? Enter your thoughts here and we will find you a restaurant!", key="name")
    st.form_submit_button("Enter", on_click=recommendation)



