import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show_rankings(df, year):
    st.sidebar.header("Ranking Options")
    n = st.sidebar.slider("Number of countries (Top/Bottom)", min_value=5, max_value=30, value=10)
    sorted_df = df.sort_values(by="Score", ascending=False)

    st.subheader(f"🏆 Top {n} Happiest Countries in {year}")
    st.dataframe(sorted_df.head(n)[['Country', 'Score']])

    st.subheader(f"😢 Bottom {n} Countries in {year}")
    st.dataframe(sorted_df.tail(n).sort_values(by="Score")[['Country', 'Score']])

def show_correlations(df):
    numeric_cols = ['Score', 'GDP', 'Health', 'Freedom', 'Trust', 'Generosity', 'Social support', 'Dystopia Residual']
    corr_df = df[numeric_cols].dropna()

    if not corr_df.empty:
        corr_matrix = corr_df.corr()
        st.subheader("📈 Correlation with Happiness Score")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(corr_matrix[['Score']].sort_values(by='Score', ascending=False),
                    annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.info("Not enough data for correlation plot.")
