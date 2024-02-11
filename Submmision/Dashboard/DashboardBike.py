# ===============================================================
#           CREATE DASHBOARD BIKE SHARING USING STREAMLIT       =
#           ---------------------------------------------       =
# Nama          : Avita Mumtahana                               =
# Email         : mumtavita@gmail.com                           =
# Id Dicoding   : dicoding.com/users/mumtavita                  =
# Github Pages  : avmum.github.io                               =
# Created       : 11 Februari 2024                              =
# ===============================================================


# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    data = pd.read_csv("hour.csv")
    return data

data = load_data()

# Set page style
st.markdown(
    """
    <style>
    .reportview-container {
        background: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set page title
st.title("Bike Share Dashboard")

# Sidebar
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Avita Mumtahana**")
st.sidebar.markdown("**• Email: [mumtavita@gmail.com](mumtavita@gmail.com)**")
st.sidebar.markdown("**• Dicoding: [Avita Mumtahana](https://www.dicoding.com/users/mumtavita/)**")
st.sidebar.markdown("**• LinkedIn: [Avita Mumtahana](https://www.linkedin.com/in/mumtavita)**")
st.sidebar.markdown("**• Github: [avmum](https://github.com/avmum)**")

st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)")

# Visualization
# Create a layout with two columns
col1, col2 = st.columns(2)


# Season-wise bike share count
season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
data["season_label"] = data["season"].map(season_mapping)
season_count = data.groupby("season_label")["cnt"].sum().reset_index()
plt.figure(figsize=(10, 10))
plt.bar(season_count["season_label"], season_count["cnt"])
plt.title("Season-wise Bike Share Count")
plt.xlabel("Season")
plt.ylabel("Count")
st.pyplot(plt)


# Weather situation-wise bike share count
weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
plt.figure(figsize=(10, 10))
plt.bar(weather_count["weathersit"], weather_count["cnt"])
plt.title("Weather Situation-wise Bike Share Count")
plt.xlabel("Weather Situation")
plt.ylabel("Count")
st.pyplot(plt)

# Hourly bike share count
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(hourly_count["hr"], hourly_count["cnt"])
plt.title("Hourly Bike Share Count")
plt.xlabel("Hour")
plt.ylabel("Count")
st.pyplot(plt)

# Humidity vs. Bike Share Count
plt.figure(figsize=(10, 6))
plt.scatter(data["hum"], data["cnt"])
plt.title("Humidity vs. Bike Share Count")
plt.xlabel("Humidity")
plt.ylabel("Count")
st.pyplot(plt)

# Wind Speed vs. Bike Share Count
plt.figure(figsize=(10, 6))
plt.scatter(data["windspeed"], data["cnt"])
plt.title("Wind Speed vs. Bike Share Count")
plt.xlabel("Wind Speed")
plt.ylabel("Count")
st.pyplot(plt)

# Temperature vs. Bike Share Count
plt.figure(figsize=(10, 6))
plt.scatter(data["temp"], data["cnt"])
plt.title("Temperature vs. Bike Share Count")
plt.xlabel("Temperature")
plt.ylabel("Count")
st.pyplot(plt)

# About
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. "
                "Dataset ini mengandung informasi mengenai penyewaan sepeda berdasarkan berbagai variabel seperti musim, suhu, kelembaban, dan faktor lainnya.")
