# World Happiness Dashboard

This interactive Streamlit app allows users to explore and compare global happiness metrics across countries and years using the World Happiness Report dataset.

 **Live App**: [https://pa-tech-lead-recr-task-7i3yivpryeeehcnpy5uv3o.streamlit.app/](https://pa-tech-lead-recr-task-7i3yivpryeeehcnpy5uv3o.streamlit.app/)

---

## Features

- **Year Selection** — Explore happiness data from 2015 to 2019
- **Filter by Region or Country** — Narrow down results dynamically
- **Top & Bottom Rankings** — Display top N and bottom N happiest countries
- **Time Trend Visualization** — Track happiness score trends across time
- **Correlation Heatmap** — Understand relationships between happiness score and its key drivers
- **Statistical Insight** — See the most influential factor per year
- **Multi-Page Layout** — Organized for clarity and scalability

---

## Tech Stack

- Python 3.9
- Streamlit
- Pandas
- Seaborn
- Plotly
- Docker (optional)
- Hosted on Streamlit Cloud

---

## Project Structure
 ```
├── Home.py # Landing page
├── pages/
│ ├── 1_Filter_and_Rank.py
│ ├── 2_Correlations.py
│ └── 3_Time_Trends.py
├── data/ 
├── data_loader.py # Cleans and unifies all data
├── filters.py # Handles sidebar filters
├── visuals.py # Contains visual components
├── requirements.txt
├── Dockerfile 
└── README.md
```


---

##  How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. (Optional) Create virtual environment
```cmd
python -m venv .venv
source .venv/Scripts/activate

pip install -r requirements.txt

streamlit run Home.py
```