import streamlit as st

if "attendance" not in st.session_state:
    st.session_state.attendance = set()

number = st.number_input("Insert your zipcode", value=None, placeholder="Type a zipcode...")
st.write('The current zipcode is ', number)

def recommendation():
    if st.session_state.name in st.session_state.attendance:
        st.info(f"{st.session_state.name} has already been counted.")
    else:
        st.session_state.attendance.add(st.session_state.name)

with st.form(key="my_form"):
    st.text_input("Any thoughts on where to eat? Enter your thoughts here and we will find you a restaurant! ", key="name")
    st.form_submit_button("enter", on_click=recommendation)

