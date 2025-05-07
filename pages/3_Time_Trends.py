import streamlit as st
import pandas as pd
import plotly.express as px
from app_files.data_loader import load_and_clean_data

st.title("📈 Time Trends of Happiness Score")

# Load and clean full dataset
df = load_and_clean_data("data")

# Filter: let user select countries
countries = sorted(df['Country'].dropna().unique())
selected_countries = st.multiselect("Select countries to compare", countries, default=["Norway", "Finland"])

if selected_countries:
    country_df = df[df['Country'].isin(selected_countries)]

    # Line chart with Plotly
    fig = px.line(
        country_df,
        x="Year",
        y="Score",
        color="Country",
        markers=True,
        title="Happiness Score Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Optional: Show GDP over time
    show_gdp = st.checkbox("Show GDP over time")
    if show_gdp:
        fig_gdp = px.line(
            country_df,
            x="Year",
            y="GDP",
            color="Country",
            markers=True,
            title="GDP Over Time"
        )
        st.plotly_chart(fig_gdp, use_container_width=True)
else:
    st.info("Please select at least one country.")
