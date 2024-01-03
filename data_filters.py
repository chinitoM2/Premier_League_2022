import streamlit as st

def filter_data(df):
  club = st.sidebar.multiselect('Pick the Club', df['Team Name'].unique())
  if not club:
    df2 = df.copy()
  else:
    df2 = df[df['Team Name'].isin(club)]

  sorted_leagues = df2['Competition'].sort_values().unique()
  league = st.sidebar.multiselect('Select League', sorted_leagues)
  if not league:
    df3 = df2.copy()
  else:
    df3 = df2[df2['Competition'].isin(league)]

  if not club and not league:
    filtered_df = df
  elif club and league:
    filtered_df = df3[df['Team Name'].isin(club) & df3['Competition'].isin(league)]
  elif club and not league:
    filtered_df = df2
  elif not club and league:
    filtered_df = df3
  else:
    filtered_df = df3[df3['Team Name'].isin(club) & df3['Competition'].isin(league)]

  return filtered_df