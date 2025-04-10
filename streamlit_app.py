import streamlit as st
from datasets import load_dataset
import pandas as pd

st.title("AG News Dataset Viewer")

# Load AG News dataset
@st.cache_data
def load_agnews_dataset():
    dataset = load_dataset("ag_news")
    return dataset

dataset = load_agnews_dataset()

# Convert to pandas DataFrame (you can choose train/test)
train_df = pd.DataFrame(dataset["train"])
test_df = pd.DataFrame(dataset["test"])

# Sidebar selection
split = st.sidebar.selectbox("Select Dataset Split", ["train", "test"])
num_rows = st.sidebar.slider("Number of rows to display", 5, 100, 10)

st.subheader(f"Displaying {split} split of AG News Dataset")

if split == "train":
    st.dataframe(train_df.head(num_rows))
else:
    st.dataframe(test_df.head(num_rows))

