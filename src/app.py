import streamlit as st
from pages.home import show_home
from pages.tokenizers import show_tokenizers

# Page configuration
st.set_page_config(
    page_title="Portfolio - Javier Vargas", page_icon="🚀", layout="wide", initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Tokenizers"])

# Page routing
if page == "Home":
    show_home()
elif page == "Tokenizers":
    show_tokenizers()
