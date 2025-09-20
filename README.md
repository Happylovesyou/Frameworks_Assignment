# 📊 CORD-19 Data Explorer (Streamlit App)

This project is a simple data analysis and visualization of the **CORD-19 metadata dataset**, built with **Python, Pandas, Matplotlib, and Streamlit**.

---

## 📂 Dataset Used
We used the **metadata.csv** file from the [CORD-19 Research Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), which contains information about COVID-19 research papers:
- Paper titles and abstracts
- Publication dates
- Authors and journals
- Sources

---

## 🛠️ Steps Followed
1. **Data Loading & Exploration**
   - Loaded metadata.csv into a Pandas DataFrame
   - Explored shape, datatypes, and missing values
2. **Data Cleaning**
   - Handled missing values in key columns (title, publish_time)
   - Converted publish_time to datetime and extracted publication year
   - Added derived features (e.g., word count in abstracts)
3. **Analysis & Visualizations**
   - Counted publications by year
   - Created bar chart of publications over time
   - Previewed filtered data in the app
4. **Streamlit App**
   - Built an interactive app with:
     - Year range slider
     - Sample data viewer
     - Publications by year bar chart

---

## 🔍 Insights Found
- The number of COVID-19 related publications **peaked in 2020**, showing the global research response to the pandemic.
- Publication trends dropped in 2021–2022 as the initial urgency slowed down.
- Most papers came from major medical and public health journals.

---

## ▶️ How to Run the Streamlit App

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Frameworks_Assignment.git
   cd Frameworks_Assignment
