import pandas as pd
import numpy as np
from fastapi import FastAPI
import re

app = FastAPI()

df_genero=pd.read_csv('Datasets/Data_Processed/def_genero.csv')
df_juegos=pd.read_csv('Datasets/Data_Processed/def_juegos.csv')
df_specs=pd.read_csv('Datasets/Data_Processed/def_specs.csv')
df_earlyacces=pd.read_csv('Datasets/Data_Processed/def_eatlyacces.csv')
df_sentiment=pd.read_csv('Datasets/Data_Processed/def_sentiment.csv')
df_metascore=pd.read_csv('Datasets/Data_Processed/def_metascore.csv')




#Endpoints of API

@app.get('/genero/{Ano}')
def genero(Ano: str):
     """
     Returns a dictionary showing the number of games by genre for a specific year.

     args:
         year (str): Year for which you want to count the video game genres.

     Returns:
         dict: Dictionary with the genres as keys and the number of video games in each genre as values.
     """

     # Check if the year contains only digits and is within the accepted range (1983 to 2019)
     if not re.match(r'^\d{4}$', Ano):
         return {"error": "Year must be a 4-digit number"}

     year = int(Ano)
     if year < 1983 or year > 2019:
         return {"error": "The year must be between 1983 and 2019"}

     # Filter the data by the selected year
     reg_year_selected = df_genero[df_genero['year'] == year]

     # Split genres that are separated by commas and remove brackets and quotes
     genres = reg_year_selected['genres'].str.split(', ')
     genre_list = [genre.strip("[]'") for sublist in genres for genre in sublist]

     # Count the number of video games by genre and create a dictionary
     genre_count = pd.Series(genre_list).value_counts()
     genre_count_dict = {genre.strip("'"): count for genre, count in genre_count.items()}

     return genre_count_dict









@app.get('/list_Games_per_year/{idioma}')
def juegos( year: str ):
    print('ok..')

@app.get('/Specs/{idioma}')
def specs( Año: str ):
    print('ok..')

@app.get('/Games_early_acces/{idioma}')
def earlyacces( Año: str ):
    print('ok..')

@app.get('/sentiment_year/{idioma}')
def sentiment( Año: str ):
    print('ok..')

@app.get('/game_meta_score/{idioma}')
def metascore( Año: str ):
    print('ok..')