import streamlit as st
from match import match  # call local module function to find matching restaurants
import pandas as pd
import plotly.express as px
import os
from dotenv import load_dotenv

st.title("Santa Barbara MealMapper: Vector-Based Dining Finder📍")
st.write("---")

# Create two columns in the Streamlit app layout
col1, col2 = st.columns(2)

image_path = "artifacts/dallelogo.png"
with col1:
    st.image(image_path)

with col2:
    st.subheader("🌟Find Your Next Dining Experience")
    with st.form(key="my_form"):
        user_input = st.text_input(
            "Any thoughts on where to eat? Enter your thoughts here, and we will find you a restaurant!"
        )
        submit_button = st.form_submit_button("Enter")

st.write("---")

# Handle form submission on the interactive dashboard.
if submit_button:
    try:
        # Obtain matching results from the 'match' function
        matching_results = match(user_input)

        # Check if any results were found and display them
        if matching_results:
            st.subheader("What we found for you:")
            for result in matching_results:
                st.markdown(f"**Name:** {result['name']}")
                st.markdown(f"**Categories:** {', '.join(result['categories'])}")
                st.markdown(f"**Address:** {result['address']}, {result['city']}")
                st.write("---")

            # Convert the matching results to a DataFrame for visualization
            restaurants_df = pd.DataFrame(matching_results)

            load_dotenv()
            MAPBOX_TOKEN = os.environ["MAPBOX_TOKEN"]
            px.set_mapbox_access_token(MAPBOX_TOKEN)

            # Create an interactive map using Plotly Express
            fig = px.scatter_mapbox(
                restaurants_df,
                lon="longitude",
                lat="latitude",
                hover_name="name",
                hover_data=["address", "city", "business_stars", "review_count"],
                color_discrete_sequence=["rgba(255, 165, 0, 0.9)"],
                size="review_count",
                size_max=15,
                zoom=10,
                title="Interactive Map",
            )

            st.plotly_chart(fig)

        else:
            st.write("No matching results found.")
    except Exception as e:
        st.error(f"Error: {e}")
