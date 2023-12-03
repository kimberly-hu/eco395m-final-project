import streamlit as st
from match import match

zipcode = st.number_input("Insert your zipcode", min_value=0, step=1, format="%i")
st.write('The current zipcode is ', zipcode)

def recommendation():
    user_query = st.session_state.name
    matching_results = match(user_query, zipcode)
    if matching_results:
        for result in matching_results:
            st.write(result)  
    else:
        st.write("No matching results found.")

with st.form(key="my_form"):
    st.text_input("Any thoughts on where to eat? Enter your thoughts here and we will find you a restaurant!", key="name")
    st.form_submit_button("Enter", on_click=recommendation)
