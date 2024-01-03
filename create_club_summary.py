import streamlit as st
import matplotlib.pyplot as plt

cmap1 = plt.cm.get_cmap('RdYlGn')
def create_club_summary(df):
  club_gf_totals_df = df.groupby(by=['Team Name'], as_index=False)['GF'].sum().sort_values(by='GF', ascending=False)
  with st.expander('Club Goals Forced Totals Summary_View Data:'):
    st.table(club_gf_totals_df.style.background_gradient(cmap=cmap1))