import streamlit as st
from app_files.data_loader import load_and_clean_data
from app_files.filters import filter_data
from app_files.visuals import show_rankings
import pandas as pd
from app_files.agent import mini_agent


st.title("📊 Filter and Rank Happiness Scores")

with st.expander("🛈 What do these variables mean?"):
    st.markdown("""
- **GDP**: Economic output per person.
- **Social support**: Having someone to count on.
- **Health**: Life expectancy at birth.
- **Freedom**: Perceived freedom to make life choices.
- **Trust**: Perception of corruption in government/business.
- **Generosity**: Willingness to donate to others.
- **Dystopia Residual**: Baseline happiness from a hypothetical worst-case society.
""")


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


st.sidebar.subheader("🧠 Ask the Dashboard")
user_q = st.sidebar.text_input("Type a question about this year's data")

if user_q:
    response = mini_agent(user_q, filtered_df, selected_year)
    st.sidebar.markdown(response)
