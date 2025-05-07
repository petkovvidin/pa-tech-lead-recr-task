import pandas as pd

def mini_agent(user_input: str, df: pd.DataFrame, year: int) -> str:
    user_input = user_input.lower()

    if "happiest" in user_input and "country" in user_input:
        top = df.sort_values(by="Score", ascending=False).iloc[0]
        return f"The happiest country in {year} was **{top['Country']}** with a score of {top['Score']:.2f}."

    elif "top" in user_input or "best" in user_input:
        top_n = df.sort_values(by="Score", ascending=False).head(5)
        countries = ", ".join(top_n['Country'].tolist())
        return f"The top 5 happiest countries in {year} were: {countries}."

    elif "most important" in user_input or "most influential" in user_input:
        numeric_cols = ['GDP', 'Social support', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']
        corr = df[numeric_cols + ['Score']].dropna().corr()['Score'].drop('Score')
        top_factor = corr.idxmax()
        return f"The most influential factor in {year} was **{top_factor}** (correlation: {corr.max():.2f})."

    elif "region" in user_input:
        if df['Region'].notna().sum() > 0:
            regions = ", ".join(sorted(df['Region'].dropna().unique()))
            return f"Available regions in {year} are: {regions}."
        else:
            return f"Region data is not available for {year}."

    else:
        return "I'm not sure how to answer that. Try asking about the happiest country, top 5, or most important factor."



"""" simple questions: 

Which was the happiest country?

Show me the top 5 countries

What was the most important factor?

What regions are available?

"""