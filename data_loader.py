import pandas as pd
import os

def load_and_clean_data(data_folder="data"):
    all_data = []

    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            year = int(filename.split(".")[0])
            file_path = os.path.join(data_folder, filename)
            df = pd.read_csv(file_path)

            # Standardize column names (strip & lower)
            df.columns = [col.strip() for col in df.columns]

            # YEAR-SPECIFIC MAPPINGS
            if year == 2015 or year == 2016:
                df = df.rename(columns={
                    "Country": "Country",
                    "Region": "Region",
                    "Happiness Score": "Score",
                    "Happiness Rank": "Rank",
                    "Economy (GDP per Capita)": "GDP",
                    "Family": "Social support",
                    "Health (Life Expectancy)": "Health",
                    "Freedom": "Freedom",
                    "Trust (Government Corruption)": "Trust",
                    "Generosity": "Generosity",
                    "Dystopia Residual": "Dystopia Residual"
                })

            elif year == 2017:
                df = df.rename(columns={
                    "Country": "Country",
                    "Happiness.Score": "Score",
                    "Happiness.Rank": "Rank",
                    "Economy..GDP.per.Capita.": "GDP",
                    "Family": "Social support",
                    "Health..Life.Expectancy.": "Health",
                    "Freedom": "Freedom",
                    "Trust..Government.Corruption.": "Trust",
                    "Generosity": "Generosity",
                    "Dystopia.Residual": "Dystopia Residual"
                })
                df["Region"] = pd.NA  # Not available in 2017

            elif year == 2018 or year == 2019:
                df = df.rename(columns={
                    "Country or region": "Country",
                    "Score": "Score",
                    "Overall rank": "Rank",
                    "GDP per capita": "GDP",
                    "Social support": "Social support",
                    "Healthy life expectancy": "Health",
                    "Freedom to make life choices": "Freedom",
                    "Perceptions of corruption": "Trust",
                    "Generosity": "Generosity"
                })
                df["Region"] = pd.NA  # Not available

            else:
                continue  # Skip unknown years

            # Add Year column
            df["Year"] = year

            # Ensure all expected columns exist
            expected_cols = [
                "Country", "Region", "Rank", "Score", "GDP", "Social support",
                "Health", "Freedom", "Trust", "Generosity", "Dystopia Residual", "Year"
            ]
            for col in expected_cols:
                if col not in df.columns:
                    df[col] = pd.NA

            df = df[expected_cols]
            all_data.append(df)

    # Combine all years
    full_df = pd.concat(all_data, ignore_index=True)
    full_df = full_df.dropna(subset=["Country", "Score", "Year"])
    return full_df
