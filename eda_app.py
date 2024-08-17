import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.api as sm


@st.cache_data
def load_data(df2):
    """Load data from a CSV file."""
    return pd.read_csv(df2)


df2 = load_data('data/nfl_team_stats_2002-2023.csv')


def run_eda_app():
    submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
    if submenu == "Descriptive":
        st.dataframe(df2)

        with st.expander("Data Types"):
            st.dataframe(df2.dtypes)

        with st.expander("Data Summary"):
            st.dataframe(df2.describe())

    elif submenu == "Plots":
        col1, col2 = st.columns([2, 2])

        with col1:
            st.subheader("Scatter Plot")
            pass

        with col2:
            model = sm.OLS(df2['score_home'], df2[['total_yards_home', 'total_yards_away']])
            results = model.fit()

            # Display the summary in Streamlit
            st.text(results.summary())