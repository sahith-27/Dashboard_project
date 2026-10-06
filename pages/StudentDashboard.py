import streamlit as st 
from helper import login_status_check,role_check


login_status_check()
role_check('student')


st.title("Student Dashboard")