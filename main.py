import pandas as pd
import numpy as np
from fastapi import FastAPI

app = FastAPI()

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