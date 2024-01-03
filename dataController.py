import streamlit as st
import pandas as pd
import io

# UPLOAD DATA FILE
def load_data():
  file = st.file_uploader(':file_folder: Upload a file', type=(['csv', 'txt', 'xlsx']))
  if file is not None:
    file_contents = file.read()
    file_buffer = io.BytesIO(file_contents)
    df = pd.read_csv(file_buffer)
    return df