import streamlit as st
import pandas as pd

st.title("AG News Dataset (Google Drive Hosted)")

@st.cache_data
def load_agnews_csv():
    url = "https://drive.google.com/file/d/1xr-eyagU6GeZlYpn8qGIuMSdK5WFUV5x/view?usp=drive_link"  # ← Replace with your real ID
    return pd.read_csv(url)

df = load_agnews_csv()

num_rows = st.slider("Rows to show", 5, 100, 10)
st.dataframe(df.head(num_rows))
