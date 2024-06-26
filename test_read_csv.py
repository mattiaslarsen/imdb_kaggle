import streamlit as st
import pandas as pd

# Läs in data från en CSV-fil
csv_file = 'C:/Users/matti/BOX/Box4/imdb_kaggle/imdb_kaggle.csv'

st.title("Filmdata Visualisering")

try:
    df = pd.read_csv(csv_file)
    st.write("CSV-filen har laddats framgångsrikt")
    st.header("De första 10 raderna av filmdatabasen")
    st.write(df.head(10))
except Exception as e:
    st.error(f"Fel vid inläsning av CSV-fil: {e}")
