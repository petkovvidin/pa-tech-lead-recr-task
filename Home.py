import streamlit as st

st.set_page_config(page_title="World Happiness Dashboard", layout="wide")
st.title("🌍 Welcome to the World Happiness Dashboard")
st.markdown("""
This app allows you to explore the World Happiness dataset across multiple years.

Use the sidebar or top menu to:
- Filter and rank countries by happiness score
- Explore correlations between happiness components
""")
