import streamlit as st

def login_status_check():
    if not st.session_state.get('status',False):
        st.title("Please login first")
        st.switch_page('app.py')

def role_check(dashboard_role:str):
    if st.session_state.get('role',"") != dashboard_role:
        st.write("Access denied")
        st.switch_page("app.py")