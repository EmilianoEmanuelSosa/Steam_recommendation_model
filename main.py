import pandas as pd
import numpy as np
from fastapi import FastAPI

app = FastAPI()

df_genero=pd.read_csv('Datasets/Data_Processed/def_genero.csv')
df_genero=pd.read_csv('Datasets/Data_Processed/def_juegos.csv')
df_genero=pd.read_csv('Datasets/Data_Processed/def_specs.csv')
df_genero=pd.read_csv('Datasets/Data_Processed/def_eatlyacces.csv')
df_genero=pd.read_csv('Datasets/Data_Processed/def_sentiment.csv')
df_genero=pd.read_csv('Datasets/Data_Processed/def_metascore.csv')




#Endpoints of API

@app.get('/genre_most_year/{idioma}')
def genero( Ano: str ):
    return 'ok'

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