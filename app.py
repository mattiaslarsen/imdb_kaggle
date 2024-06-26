import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sätt titeln på Streamlit-appen
st.title("Filmdata Visualisering")

# Ange relativ sökväg till CSV-filen
csv_file = 'imdb_kaggle.csv'

# Försök att läsa in data från CSV-filen
try:
    df = pd.read_csv(csv_file)
    st.write("CSV-filen har laddats framgångsrikt")
    
    # Visa de första 10 raderna av datan
    st.header("De första 10 raderna av filmdatabasen")
    st.dataframe(df.head(10))  # Använd dataframe för visning

    # Filtrera data för de senaste 10 åren
    latest_year = df['year'].max()
    last_10_years = df[df['year'] >= (latest_year - 10)]

    # Räkna antalet filmer per år för de senaste 10 åren
    films_per_year = last_10_years['year'].value_counts().sort_index()

    # Skapa ett stapeldiagram
    st.header("Antal filmer per år för de senaste 10 åren")
    fig, ax = plt.subplots()
    ax.bar(films_per_year.index, films_per_year.values)
    ax.set_xlabel('År')
    ax.set_ylabel('Antal filmer')
    ax.set_title('Antal filmer per år för de senaste 10 åren')
    st.pyplot(fig)

except Exception as e:
    # Hantera eventuella fel vid inläsning av CSV-filen
    st.error(f"Fel vid inläsning av CSV-fil: {e}")


