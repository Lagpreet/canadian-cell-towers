# Jagpreet Sekhon May 2024
# Canadian Cell Towers - web app to view cell tower location and details.
# Data provided by ISED publicly.
import folium
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static

# Set title and page layout
st.title('Canadian Cell Towers Map')
st.sidebar.title('Options')
st.sidebar.write('No options available right now')

# Function to load data from uploaded CSV file
@st.cache_data
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file, encoding='latin1')

# File uploader
uploaded_file = st.file_uploader("Please upload a CSV file.", type="csv")

if uploaded_file is not None:
    # Load data
    data = load_data(uploaded_file)

    # Create a Folium map centered on Canada
    map = folium.Map(location=[56.1304, -106.3468], zoom_start=4)

    # Filter out rows with NaN values in Latitude and Longitude columns
    data = data.dropna(subset=['LATITUDE', 'LONGITUDE'])

    # Add markers for each cell tower
    for index, row in data.iterrows():
        folium.Marker([row['LATITUDE'], row['LONGITUDE']], popup=row['LICENSEE']).add_to(map)

    # Display the map using Streamlit
    folium_static(map)
else:
    st.write("Please upload the latest CSV file from ISED for all Spectrum data.")
