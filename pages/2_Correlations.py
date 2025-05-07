import streamlit as st
from app_files.data_loader import load_and_clean_data
from app_files.filters import filter_data
from app_files.visuals import show_correlations

st.title("📈 Correlation Between Happiness Score and Factors")

df = load_and_clean_data("data")
filtered_df, selected_year = filter_data(df)

show_correlations(filtered_df)
