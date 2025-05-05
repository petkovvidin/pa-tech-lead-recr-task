import streamlit as st
from data_loader import load_and_clean_data
from filters import filter_data
from visuals import show_rankings, show_correlations

st.set_page_config(layout="wide")
st.title("🌍 World Happiness Dashboard")

# Load data
df = load_and_clean_data("data")

# Filter data
filtered_df, selected_year = filter_data(df)

# Show filtered data
st.subheader(f"Happiness Data for {selected_year}")
st.write(f"Total countries shown: {len(filtered_df)}")
st.dataframe(filtered_df)

# Visualizations
show_rankings(filtered_df, selected_year)
show_correlations(filtered_df)
