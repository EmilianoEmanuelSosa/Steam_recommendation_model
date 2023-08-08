import pandas as pd
import pickle


# Calculate the mode of the 'genres' column
def get_mode_list(lst):
    # Use the Counter class from collections to count the occurrences of each list in the 'genres' column
    from collections import Counter
    counter = Counter(lst)
    # Find the most common list (the mode) and return it
    mode_list = counter.most_common(1)[0][0]
    return mode_list

def join_genres(genre_list):
    return " ".join(genre_list).replace("[", "").replace("]", "").replace("'", "")




def sort_dict(dict_to_sort, ascending=False):
  return {k: v for k, v in list(sorted(dict_to_sort.items(), key=lambda item: item[1], reverse=~ascending))[:5]}


def load_data():
  """
  Abre un archivo serializado y retorna el objeto cargado
  """
  dbfile = open('api/pkl/steam_games.pkl', 'rb')
  df = pd.read_pickle(dbfile)
  dbfile.close()
  return df

def load_model():
  """
  Abre el arcrvivo con
  """  
  modelfile = open('api/pkl/fitted_model.pkl', 'rb')
  model = pickle.load(modelfile)
  modelfile.close()
  return model

def count_items(items_dict, list_items, none_value=None):
  
  if isinstance(list_items, str):
    print(list_items)
    if list_items == none_value:
      return

    for item in list(literal_eval(list_items)):
      if item in items_dict:
        items_dict[item] += 1
      else:
        items_dict[item] = 1

##############

def get_game(id):
  """
  """
  df = load_data()

  try:
    game = df[df['id'] == int(id)].to_dict(orient='records')[0]
    return game
  except: 
    return {
      'error': f'Game {id} not found'
    }
  
  
##############

def get_game_list(year, limit=10000):
  """
  Se ingresa un año y devuelve una lista con los juegos lanzados en el año.
  """
  df = load_data()
  games_list = df[df['release_date'].dt.year  == int(year)]
  games_dict = games_list.head(limit).to_dict(orient='records')
  return games_dict

##############

def get_specs_dict(year):
  """
  """
  
  df = load_data()
  specs_dict = {}
  
  df = df[df['release_date'].dt.year == int(year)]
  df['specs'].map(lambda x: count_items(specs_dict, x, 'no_specs'))

  return sort_dict(specs_dict)

##############

def get_sentiment_dict(year):
  """
  """
  df = load_data()
  sentiment_dict = {}
  
  def count_sentiment(sentiment):
    if sentiment == 'no_sentiment':
      return
    if sentiment in sentiment_dict:
      sentiment_dict[sentiment] += 1
    else:
      sentiment_dict[sentiment] = 1
 
  df = df[df['release_date'].dt.year == int(year)]
  df['sentiment'].map(lambda x: count_sentiment(x))
  return sentiment_dict


##############

def get_genres_dict(year):
  """
  """
  
  df = load_data()
  genres_dict = {}
  
  df = df[df['release_date'].dt.year == int(year)]
  df['genres'].map(lambda x: count_items(genres_dict, x, 'no_genres_registered'))
  return sort_dict(genres_dict)


##############

def get_early_access(year):
  """
  """
  df = load_data()
  
  df = df[df['early_access'] == True]
  df = df[df['release_date'].dt.year == int(year)]
  game_list = df.to_dict(orient='records')
  return [df.shape[0], game_list]


##############

def get_metascore(year: int, limit=10000, ) -> list:
  """
  """
  
  df = load_data()
  df = df[df['release_date'].dt.year == int(year)]
  df = df[df['metascore'] != 'no_score']
  df = df.sort_values(by=['metascore'], ascending=False)
  top_games = df.head(limit)
  top_games_dict = top_games.to_dict(orient='records')
  return top_games_dict



def load_data():
  """
  Abre un archivo serializado y retorna el objeto cargado
  """
  dbfile = open('../Datasets/Data_Processed/steam_games.pkl', 'rb')
  df = pd.read_pickle(dbfile)
  dbfile.close()
  return df


def load_model():
  """
  Abre el arcrvivo con
  """  
  modelfile = open('/home/mkm/programin/Steam_recommendation_model/Datasets/Data_Processed/fitted_model.pkl', 'rb')
  model = pickle.load(modelfile)
  modelfile.close()
  return model

def count_items(items_dict, list_items, none_value=None):
  
  if isinstance(list_items, str):
    print(list_items)
    if list_items == none_value:
      return

    for item in list(literal_eval(list_items)):
      if item in items_dict:
        items_dict[item] += 1
      else:
        items_dict[item] = 1

##############

def get_game(id):
  """
  """
  df = load_data()

  try:
    game = df[df['id'] == int(id)].to_dict(orient='records')[0]
    return game
  except: 
    return {
      'error': f'Game {id} not found'
    }
  
  
##############

def get_game_list(year, limit=10000):
  """
  Se ingresa un año y devuelve una lista con los juegos lanzados en el año.
  """
  df = load_data()
  games_list = df[df['release_date'].dt.year  == int(year)]
  games_dict = games_list.head(limit).to_dict(orient='records')
  return games_dict

##############

def get_specs_dict(year):
  """
  """
  
  df = load_data()
  specs_dict = {}
  
  df = df[df['release_date'].dt.year == int(year)]
  df['specs'].map(lambda x: count_items(specs_dict, x, 'no_specs'))

  return sort_dict(specs_dict)

##############

def get_sentiment_dict(year):
  """
  """
  df = load_data()
  sentiment_dict = {}
  
  def count_sentiment(sentiment):
    if sentiment == 'no_sentiment':
      return
    if sentiment in sentiment_dict:
      sentiment_dict[sentiment] += 1
    else:
      sentiment_dict[sentiment] = 1
 
  df = df[df['release_date'].dt.year == int(year)]
  df['sentiment'].map(lambda x: count_sentiment(x))
  return sentiment_dict


##############

def get_genres_dict(year):
  """
  """
  
  df = load_data()
  genres_dict = {}
  
  df = df[df['release_date'].dt.year == int(year)]
  df['genres'].map(lambda x: count_items(genres_dict, x, 'no_genres_registered'))
  return sort_dict(genres_dict)


##############

def get_early_access(year):
  """
  """
  df = load_data()
  
  df = df[df['early_access'] == True]
  df = df[df['release_date'].dt.year == int(year)]
  game_list = df.to_dict(orient='records')
  return [df.shape[0], game_list]


##############

def get_metascore(year: int, limit=10000, ) -> list:
  """
  """
  
  df = load_data()
  df = df[df['release_date'].dt.year == int(year)]
  df = df[df['metascore'] != 'no_score']
  df = df.sort_values(by=['metascore'], ascending=False)
  top_games = df.head(limit)
  top_games_dict = top_games.to_dict(orient='records')
  return top_games_dict