import streamlit as st
import pandas as pd
from dataController import load_data
from data_filters import filter_data
from create_club_summary import create_club_summary

def main():
  st.set_page_config(page_title='2022 Premier League ⚽️⚽️', page_icon=':bar_chart', layout='wide')
  st.title('2022-2023 Premier League')
  st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

  # UPLOAD DATA
  df = load_data()

  col_StartDate, col_EndDate = st.columns((2))
  df['Date'] = pd.to_datetime(df['Date'])
  startDate = pd.to_datetime(df['Date']).min()
  endDate = pd.to_datetime(df['Date']).max()
  with col_StartDate:
    date1 = pd.to_datetime(st.date_input('Start Date', startDate))
  with col_EndDate:
    date2 = pd.to_datetime(st.date_input('End Date', endDate))
  df = df[(df['Date'] >= date1) & (df['Date'] <= date2)].copy()

  # DATA FILTERS
  st.sidebar.header('Choose your filter: ')
  filtered_df = filter_data(df)

  # DATA REPORTS AND VISUALIZATIONS
  with st.expander('Club Table Summary_View Data: '):
    st.table(filtered_df)
  create_club_summary(filtered_df)

if __name__ == '__main__':
  main()

