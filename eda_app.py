import streamlit as st
# import pandas as pd


# @st.cache_data
# def load_data(df1):
#     return pd.read_pickle(df1)

# df1 = load_data('data/nfl_team_stats_2002_2023.pkl')

def run_eda_app():
    st.subheader("Exploratory Data Analysis")
    # submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
    # if submenu == "Descriptive":
    #     st.dataframe(df1)

    #     with st.expander("Data Types"):
    #         st.dataframe(df1.dtypes)

    #     with st.expander("Data Summary"):
    #         st.dataframe(df1.describe())

    # elif submenu == "Plots":
    #     st.subheader("Plots for Our Data")
    #     col1, col2 = st.columns([2, 1])

    #     with col1:
    #         with st.bar_chart(df1):
    #             pass
            
        


