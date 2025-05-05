# World Happiness Dashboard

This Streamlit app allows users to explore and compare happiness metrics across countries and years, using data from the World Happiness Report.

##  Features

-> Filter by year, region, and country  
-> View happiness rankings (top N / bottom N)  
-> See correlations between happiness score and components  
-> Compare happiness trends over time for selected countries  
-> Multi-page layout for clean navigation  

##  Tech Stack

- Python 3.9+
- Streamlit
- Pandas
- Plotly
- Seaborn

## Project Structure
pa-tech-lead-recr-task/
    ├── Home.py # Main landing page
    ├── pages/
    │ ├── 1_Filter_and_Rank.py
    │ ├── 2_Correlations.py
    │ └── 3_Time_Trends.py
    ├── data/ 
    ├── data_loader.py
    ├── filters.py
    ├── visuals.py
    ├── requirements.txt
    └── README.md


