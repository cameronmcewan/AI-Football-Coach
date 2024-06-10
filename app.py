import streamlit as st
from football_drills import football_drills

# Set the title of the app
st.title("AI Football Coach")

# Create sidebar 
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Football Drills"])

# Define functions for each page
def home():
    st.header("Welcome to AI Football Coach")
    st.write("This tool provides AI generate content to support football coaches working at all levels from grassroots to the professional game.")


# Display the selected page 
if page == "Home":
    home()
elif page == "Football Drills":
    football_drills()



# Footer 
st.sidebar.markdown("---")
st.sidebar.markdown("AI Football Coach © 2024")