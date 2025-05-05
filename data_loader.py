import pandas as pd
import os

def load_and_clean_data(data_folder="data"):
    all_data = []

    column_mapping = {
        'Country': 'Country', 'Country name': 'Country',
        'Happiness.Score': 'Score', 'Happiness Score': 'Score', 'Happiness score': 'Score', 'Score': 'Score',
        'Happiness Rank': 'Rank', 'Happiness.Rank': 'Rank', 'Overall rank': 'Rank',
        'Region': 'Region',
        'Economy (GDP per Capita)': 'GDP', 'Logged GDP per capita': 'GDP',
        'Health (Life Expectancy)': 'Health', 'Healthy life expectancy': 'Health',
        'Freedom': 'Freedom', 'Freedom to make life choices': 'Freedom',
        'Trust (Government Corruption)': 'Trust', 'Perceptions of corruption': 'Trust',
        'Generosity': 'Generosity',
        'Family': 'Social support', 'Social support': 'Social support',
        'Dystopia Residual': 'Dystopia Residual'
    }

    expected_cols = ['Country', 'Region', 'Score', 'Rank', 'GDP', 'Health', 'Freedom', 'Trust', 'Generosity', 'Social support', 'Dystopia Residual']

    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            year = int(filename.split(".")[0])
            df = pd.read_csv(os.path.join(data_folder, filename))
            df.columns = [col.strip() for col in df.columns]
            df = df.rename(columns=column_mapping)
            for col in expected_cols:
                if col not in df.columns:
                    df[col] = pd.NA
            df['Year'] = year
            all_data.append(df[expected_cols + ['Year']])
    
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df = combined_df.dropna(subset=['Country', 'Score'])
    return combined_df
