import streamlit as st
from data_loader import load_and_clean_data
from filters import filter_data
from visuals import show_rankings
import pandas as pd


st.title("📊 Filter and Rank Happiness Scores")

df = load_and_clean_data("data")
filtered_df, selected_year = filter_data(df)

st.subheader(f"Data for {selected_year}")
st.dataframe(filtered_df)

show_rankings(filtered_df, selected_year)


# Correlation-based insight
numeric_cols = ['GDP', 'Social support', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']
insight_df = filtered_df[numeric_cols + ['Score']].dropna()

if not insight_df.empty:
    corr_series = insight_df.corr()['Score'].drop('Score').sort_values(ascending=False)
    top_factor = corr_series.idxmax()
    top_corr = corr_series.max()
    st.markdown(f"🧠 **Insight:** In {selected_year}, the factor most correlated with Happiness Score was **{top_factor}** with a correlation of **{top_corr:.2f}**.")
else:
    st.info("Not enough numeric data available to compute insights.")
