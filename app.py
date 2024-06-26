import streamlit as st
import pandas as pd

# Sätt titeln på Streamlit-appen
st.title("Filmdata Visualisering")

# Ange sökvägen till din CSV-fil
csv_file = 'imdb_kaggle.csv'

# Försök att läsa in data från CSV-filen
try:
    df = pd.read_csv(csv_file)
    st.write("CSV-filen har laddats framgångsrikt")
    
    # Visa de första 10 raderna av datan
    st.header("De första 10 raderna av filmdatabasen")
    st.dataframe(df.head(10))  # Använd dataframe för visning
except Exception as e:
    # Hantera eventuella fel vid inläsning av CSV-filen
    st.error(f"Fel vid inläsning av CSV-fil: {e}")

