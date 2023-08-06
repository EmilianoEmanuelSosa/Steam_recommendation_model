import pandas as pd
import numpy as np
from fastapi import FastAPI

app = FastAPI()

df_genero=pd.read_csv('Datasets/Data_Processed/def_genero.csv')
df_juegos=pd.read_csv('Datasets/Data_Processed/def_juegos.csv')
df_specs=pd.read_csv('Datasets/Data_Processed/def_specs.csv')
df_earlyacces=pd.read_csv('Datasets/Data_Processed/def_eatlyacces.csv')
df_sentiment=pd.read_csv('Datasets/Data_Processed/def_sentiment.csv')
df_metascore=pd.read_csv('Datasets/Data_Processed/def_metascore.csv')




#Endpoints of API

@app.get('/genre_most_year/{idioma}')
def genero( Ano: str ):
    reg_year_selected=df_genero[df_genero['year']==int(Ano)]
        # Count the values in the desired column
        genre_counts = df_genero['genre'].explode().value_counts()
        # Count the values in the desired column
        genre_counts = df_genero['genres'].explode().value_counts()

        # Create the dictionary from the string
        gender_count_dict = genre_counts.to_dict()
        return gender_count_dict

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