# app.py
# Streamlit Web App for Exploring the CORD-19 Dataset

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# --- Load dataset ---
df = pd.read_csv("metadata.csv")
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year
df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))

# --- Streamlit App Layout ---
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# --- Interactive Filter: Year Range ---
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# --- Show Data Sample ---
st.subheader("Sample Data")
st.write(filtered.head())

# --- Visualization: Publications by Year ---
st.subheader("Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
ax.set_title("COVID-19 Publications per Year")
st.pyplot(fig)

# --- Visualization: Top 10 Journals ---
st.subheader("Top 10 Journals")
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax, palette="viridis")
ax.set_xlabel("Number of Publications")
ax.set_ylabel("Journal")
ax.set_title("Top Journals Publishing COVID-19 Papers")
st.pyplot(fig)

# --- Visualization: Word Cloud ---
st.subheader("Word Cloud of Paper Titles")
all_titles = " ".join(filtered["title"].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_titles)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# --- Visualization: Abstract Word Count Distribution ---
st.subheader("Abstract Word Count Distribution")
fig, ax = plt.subplots()
ax.hist(filtered["abstract_word_count"], bins=50, color="skyblue", edgecolor="black")
ax.set_xlabel("Word Count")
ax.set_ylabel("Number of Papers")
ax.set_title("Distribution of Abstract Word Counts")
st.pyplot(fig)
