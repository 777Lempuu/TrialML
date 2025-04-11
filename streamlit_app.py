import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

st.set_page_config(page_title="AG News Dataset Viewer", layout="wide")
st.title("📰 AG News Dataset Viewer & Visualizer")

@st.cache_data
def load_agnews_csv():
    url = "https://drive.google.com/uc?id=1xr-eyagU6GeZlYpn8qGIuMSdK5WFUV5x"
    return pd.read_csv(url)

# Load data
df = load_agnews_csv()

st.write("### 🔍 Data Preview")
num_rows = st.slider("Number of rows to display", 5, 100, 10)
st.dataframe(df.head(num_rows))

# Check if label column exists
label_col = 'Class Index' if 'Class Index' in df.columns else df.columns[0]
text_col = 'Title' if 'Title' in df.columns else df.columns[1]

# Show class distribution
st.write("### 📊 Class Distribution")
class_counts = df[label_col].value_counts().sort_index()
st.bar_chart(class_counts)

# Visualization: Text embedding using TF-IDF + PCA
st.write("### 🎨 2D Visualization of News Titles")

sample_size = st.slider("Number of samples to visualize", 100, min(2000, len(df)), 500, step=100)

# Sample and vectorize
sampled_df = df.sample(sample_size, random_state=42)
tfidf = TfidfVectorizer(max_features=200)
X_tfidf = tfidf.fit_transform(sampled_df[text_col])

# PCA for dimensionality reduction
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_tfidf.toarray())

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    x=X_pca[:, 0], y=X_pca[:, 1],
    hue=sampled_df[label_col].astype(str),
    palette="tab10",
    alpha=0.7,
    ax=ax
)
ax.set_title("2D PCA Scatter Plot of TF-IDF Features")
ax.set_xlabel("PCA 1")
ax.set_ylabel("PCA 2")
st.pyplot(fig)
