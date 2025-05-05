import streamlit as st
from data_loader import load_and_clean_data
from filters import filter_data
from visuals import show_rankings

st.title("📊 Filter and Rank Happiness Scores")

df = load_and_clean_data("data")
filtered_df, selected_year = filter_data(df)

st.subheader(f"Data for {selected_year}")
st.dataframe(filtered_df)

show_rankings(filtered_df, selected_year)
