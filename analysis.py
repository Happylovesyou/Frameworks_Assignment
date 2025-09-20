# analysis.py
# Basic analysis of the CORD-19 dataset (metadata.csv)
# ----------------------------------------------------
# This script demonstrates:
# 1. Data loading and exploration
# 2. Data cleaning and preparation
# 3. Simple analysis and visualization

# --- 1. DATA LOADING AND EXPLORATION ---

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

# Load dataset (make sure metadata.csv is in the same folder as this file)
df = pd.read_csv("metadata.csv")

# Show basic shape of the dataset (rows, columns)
print("Dataset shape:", df.shape)

# Show data types of each column
print("\nData types:")
print(df.dtypes)

# Check missing values in each column
print("\nMissing values per column:")
print(df.isnull().sum())

# Basic statistical summary (only for numerical columns)
print("\nBasic statistics:")
print(df.describe())

# Preview the first few rows of the dataset
print("\nFirst 5 rows:")
print(df.head())

# --- 2. CLEANING AND PREPARATION ---

# Drop rows where title or publish_time is missing
df = df.dropna(subset=["title", "publish_time"])

# Convert publish_time column to datetime format
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract publication year for analysis
df["year"] = df["publish_time"].dt.year

# --- 3. ANALYSIS AND VISUALIZATION ---

# (a) Publications by year
year_counts = df["year"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.show()

# (b) Top 10 journals publishing COVID-19 papers
top_journals = df["journal"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis")
plt.title("Top 10 Journals Publishing COVID-19 Papers")
plt.xlabel("Number of Publications")
plt.ylabel("Journal")
plt.show()

# (c) Word frequency in titles
# Combine all titles into one string
all_titles = " ".join(df["title"].astype(str))

# Split into words and count frequencies
word_counts = Counter(all_titles.lower().split())

# Get the 20 most common words
common_words = word_counts.most_common(20)

# Convert to DataFrame for plotting
word_df = pd.DataFrame(common_words, columns=["word", "count"])

plt.figure(figsize=(10, 6))
sns.barplot(x="count", y="word", data=word_df, palette="mako")
plt.title("Most Frequent Words in Paper Titles")
plt.xlabel("Frequency")
plt.ylabel("Word")
plt.show()
