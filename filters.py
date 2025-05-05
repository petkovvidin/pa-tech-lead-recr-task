import streamlit as st

def filter_data(df):
    st.sidebar.header("📊 Filter Options")

    # Year
    years = sorted(df['Year'].unique(), reverse=True)
    selected_year = st.sidebar.selectbox("Select Year", years)
    df = df[df['Year'] == selected_year]

    # Region
    regions = ['All'] + sorted(df['Region'].dropna().unique())
    selected_region = st.sidebar.selectbox("Select Region", regions)
    if selected_region != 'All':
        df = df[df['Region'] == selected_region]

    # Country
    countries = sorted(df['Country'].dropna().unique())
    selected_countries = st.sidebar.multiselect("Select Countries", countries)
    if selected_countries:
        df = df[df['Country'].isin(selected_countries)]

    return df, selected_year
