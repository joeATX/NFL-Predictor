import streamlit as st
import pandas as pd
from eda_app import run_eda_app

@st.cache_data
def load_data(df1):
    """Load data from a CSV file."""
    return pd.read_csv(df1)

desc_temp = """
    #### NFL Predictor App
    This dataset contains the most current NFL team statistics.

    #### About the Dataset
    This dataset provides the weekly stats from NFL games from the time period of 2002-2023. The weekly data is helpful
    because it allows us the insight to why they beat certain teams and not others.

    The data is sourced from:
    - ** National Football League website
    - ** Dataset provided by https://www.kaggle.com/

    #### Data Processing
    - ** Data Cleaning
    - Handling missing values in columns such as 'yards_away', 'yards_home', and 'filtered_week'.
    - Converting string data in columns like 'redzone_comp_away', 'redzone_att_away', 
    and 'possession_home' into appropriate numeric formats for analysis.
    - Splitting and converting compound string data (e.g., 'redzone_comp_away' and 'redzone_att_away') 
    into separate columns to capture distinct metrics such as completions, attempts, and success rates.

    - **Standardizing Variables:
    - Converting time-related data (e.g., 'date') into a consistent datetime format.  
    - Ensuring consistency across columns representing similar metrics for home and away teams, 
    such as 'yards_home' and 'yards_away'.
    - Standardizing units and formats to enable straightforward comparison and analysis. 

    - **Data Transformation:
    - Transforming specific columns (e.g., 'possession_home' and 'possession_away') into seconds 
    to enable time-based analysis.
    - Creating additional columns and metrics to reflect detailed game outcomes, such as win/loss indicators.

    - **Metadata Addition:
    - Adding necessary metadata to ensure all columns and derived metrics are clearly labeled and described.
    - Ensuring that each metric is accompanied by appropriate context, such as game week, season, and team information.

    - **Dataset Source:** Kaggle

    #### Datasource
     - https://www.kaggle.com/datasets/cviaxmiwnptr/nfl-team-stats-20022019-espn 

    #### App Content
    - EDA Section: Exploratory Data Analysis
    - ML Section: ML Predictor App
    """

def main():
    menu = ["Home", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        st.write(desc_temp)
    elif choice == "EDA":
        st.subheader("Exploratory Data Analysis")
        run_eda_app()
    elif choice == "ML":
        pass
    else:
        st.subheader("About")