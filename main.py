import pandas as pd
import numpy as np
from fastapi import FastAPI
import re
from collections import Counter

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


@app.get('/juegos/{year}')
def juegos(year: str):
    """
    Returns a list of games released in a specific year.

    Args:
        year (str): Year for which you want to retrieve the list of games.

    Returns:
        list: List of games released in the specified year.
    """
    # Check if the year contains only digits and is within the accepted range (e.g., 1983 to 2019)
    if not re.match(r'^\d{4}$', year):
        return {"error": "Year must be a 4-digit number"}

    # Convert the year to an integer for filtering
    year = int(year)

    # Check if the year is within the accepted range (1983 to 2019)
    if year < 1983 or year > 2019:
        return {"error": "The year must be between 1983 and 2019"}

    # Filter the data by the selected year
    games_by_year = [(row['app_name'], row['year']) for index, row in df_juegos.iterrows() if row['year'] == year]

    # Extract the game names from the filtered data
    game_names = [game[0] for game in games_by_year]

    return game_names




from collections import Counter
import ast

@app.get('/Specs/{Ano}')
def specs(Ano: str):
    """
    Returns a dictionary with the 5 most repeated specs for a specific year.

    Args:
        Ano (str): Year for which you want to count the specs.

    Returns:
        dict: Dictionary with the year as key and a list of strings containing the spec.
    """
    # Check if the year contains only digits and is within the accepted range (e.g., 1983 to 2019)
    if not re.match(r'^\d{4}$', Ano):
        return {"error": "Year must be a 4-digit number"}

    # Convert the year to an integer for filtering
    year = int(Ano)

    # Check if the year is within the accepted range (1983 to 2019)
    if year < 1983 or year > 2019:
        return {"error": "The year must be between 1983 and 2019"}

    # Filter the data by the selected year
    specs_by_year = [row['specs'] for index, row in df_specs.iterrows() if row['year'] == year]

    # Convert lists to strings and count their occurrences
    specs_count = Counter([str(spec) for spec in specs_by_year])

    # Get the top 5 specs as a list of strings containing the spec
    top_specs_list = [spec.strip('[]') for spec, _ in specs_count.most_common(5)]

    # Create the final dictionary structure
    result_dict = {str(year): top_specs_list}

    return result_dict









@app.get('/earlyacces/{Ano}')
def earlyacces(Ano: str):
    """
    Returns the number of games released with early access in a specific year.

    Args:
        Ano (str): Year for which you want to count the games with early access.

    Returns:
        dict: Dictionary with the year as key and the number of games with early access as value.
    """
    # Check if the year contains only digits and is within the accepted range (e.g., 1983 to 2019)
    if not re.match(r'^\d{4}$', Ano):
        return {"error": "Year must be a 4-digit number"}

    # Convert the year to an integer for filtering
    year = int(Ano)

    # Check if the year is within the accepted range (1983 to 2019)
    if year < 1983 or year > 2019:
        return {"error": "The year must be between 1983 and 2019"}

    # Filter the data by the selected year and early access flag
    games_with_early_access = df_earlyacces[(df_earlyacces['year'] == year) & (df_earlyacces['early_access'] == True)]

    # Get the count of games with early access
    count_early_access = len(games_with_early_access)

    # Create the final dictionary structure
    result_dict = {str(year): count_early_access}

    return result_dict




@app.get('/sentiment_year/{Ano}')
def sentiment(Ano: str):
    """
    Returns a dictionary with the count of sentiment categories for a specific year.

    Args:
        Ano (str): Year for which you want to count the sentiment categories.

    Returns:
        dict: Dictionary with the sentiment category as key and the count as value, ordered by count in descending order,
              excluding the categories with "user reviews" in the key.
    """
    # Check if the year contains only digits and is within the accepted range (e.g., 1983 to 2019)
    if not re.match(r'^\d{4}$', Ano):
        return {"error": "Year must be a 4-digit number"}

    # Convert the year to an integer for filtering
    year = int(Ano)

    # Check if the year is within the accepted range (1983 to 2019)
    if year < 1983 or year > 2019:
        return {"error": "The year must be between 1983 and 2019"}

    # Filter the data by the selected year and sentiment column
    sentiments_by_year = [row['sentiment'] for index, row in df_sentiment.iterrows() if row['year'] == year]

    # Count the occurrences of each sentiment category
    sentiment_count = Counter(sentiments_by_year)

    # Remove categories with "user reviews" in the key
    filtered_sentiment = {k: v for k, v in sentiment_count.items() if "user reviews" not in k}

    # Sort the sentiment categories by count in descending order
    sorted_sentiment = dict(sorted(filtered_sentiment.items(), key=lambda x: x[1], reverse=True))

    return sorted_sentiment





@app.get('/game_meta_score/{Ano}')
def metascore(Año: str):
    """
    Returns a dictionary with the top 5 games for a specific year with the highest metascore.

    Args:
        Año (str): Year for which you want to find the top 5 games.

    Returns:
        dict: Dictionary with the game name as key and its metascore as value, for the top 5 games of the specified year.
    """
    # Check if the year contains only digits and is within the accepted range (e.g., 1983 to 2019)
    if not re.match(r'^\d{4}$', Año):
        return {"error": "Year must be a 4-digit number"}

    # Convert the year to an integer for filtering
    year = int(Año)

    # Check if the year is within the accepted range (1983 to 2019)
    if year < 1983 or year > 2019:
        return {"error": "The year must be between 1983 and 2019"}

    # Filter the data by the selected year
    games_by_year = df_metascore[df_metascore['year'] == year]

    # Drop rows with missing values in metascore
    games_by_year = games_by_year.dropna(subset=['metascore'])

    # Convert the metascore column to numeric values
    games_by_year['metascore'] = pd.to_numeric(games_by_year['metascore'], errors='coerce')

    # Sort the games by metascore in descending order
    sorted_games = games_by_year.sort_values(by='metascore', ascending=False)

    # Take the top 5 games with the highest metascore
    top_5_games = sorted_games.head(5)

    # Create a dictionary with game name as key and metascore as value for each of the top 5 games
    top_5_dict = {row['app_name']: row['metascore'] for _, row in top_5_games.iterrows()}

    return top_5_dict