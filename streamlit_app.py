import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AG News Viewer", layout="wide")
st.title("📰 AG News Dataset Viewer")

# Load CSV with cache
@st.cache_data
def load_agnews_csv():
    url = "https://drive.google.com/uc?id=1xr-eyagU6GeZlYpn8qGIuMSdK5WFUV5x"
    return pd.read_csv(url)

df = load_agnews_csv()

# Show raw data
st.write("### 🔍 Data Preview")
num_rows = st.slider("Number of rows to display", 5, 100, 10)
st.dataframe(df.head(num_rows))

# Identify label column
label_col = 'Class Index' if 'Class Index' in df.columns else df.columns[0]
text_col = 'Title' if 'Title' in df.columns else df.columns[1]

# Bar plot of class distribution
st.write("### 📊 Distribution of News Categories")

fig, ax = plt.subplots()
df[label_col].value_counts().sort_index().plot(kind='bar', color='skyblue', ax=ax)
ax.set_xlabel("Class Index")
ax.set_ylabel("Number of Samples")
ax.set_title("Number of Samples per News Category")
st.pyplot(fig)
