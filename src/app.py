import streamlit as st
from pages.home import show_home
from pages.tokenizers import show_tokenizers

# Page configuration
st.set_page_config(
    page_title="Portfolio - Javier Vargas", page_icon="🚀", layout="wide", initial_sidebar_state="expanded"
)

# Define pages using st.Page
home_page = st.Page(show_home, title="Home", icon="🏠")
tokenizers_page = st.Page(show_tokenizers, title="Tokenizers", icon="🔤")

# Create navigation
pg = st.navigation([home_page, tokenizers_page])

# Run the selected page
pg.run()
