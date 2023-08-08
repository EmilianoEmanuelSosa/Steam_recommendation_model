<br></br>

# steam_recommendation_model

<br></br>

---

<br></br>

<div style="text-align: left; float: left;">_________________________________Project Description_____________________________________</div>

<br></br>
<br></br>
The objective of this project is to generate an API, where the Steam dataset can be consumed, it is also required to produce a Machine Learning Model which will be focused and designed to predict the sale price of a steam game.
<br></br>

---

# Project workflow

<br></br>

![Alt text](https://raw.githubusercontent.com/Rickhersd/Steam_games_API_services/main/imgs/ProcessFlowConceptualDiagram.png)

---

## Data source:

- [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj?usp=drive_link): Folder with the datasets to use.
- **Data dictionary**: Dictionary with some descriptions of the columns available in the dataset.

![Alt Text](https://raw.githubusercontent.com/Rickhersd/Steam_games_API_services/main/imgs/Data-dict.png)

---

## Technologies used in this project:

- **Scikit-learn**
- **Panda**
- **Matplotlib**
- **Numpy**
- **Flask**
- **uvicorn**
- **Seaborn**
- **Modin**
- **FastApi**
- **Pickle**

## <br></br>

---

## Project Folder:

- #### DataSets: All the datasets available for analysis are stored in this folder.
  - #### Data Ingested: Raw data is stored in this folder.
    - STEAM Data Dictionary.xlsx
      -steam_games.json
  - #### Data Processes: The processed data is stored in this folder.
    -def_eatlyaccess.csv
    - def_genre.csv
    - def_games.csv
      -def_metascore.csv
      -def_sentiment.csv
      -def_specs.csv
      -Model_Price_1.csv
      -Steam_For_Eda.csv
  - #### EDA_ET: All the files ingested and processed from the ETL, EDA and modeling process are stored in this folder.
    -eda.ipynb
    -modeling.ipynb
    - transformations.ipynb
    - utils.py: module created to host necessary functions for EDA, ETL and modeling.
    - README.md: File where this is being displayed.
      <br></br>
- #### .gitignore: This file ignores files that are not relevant to the project but were needed to make it.
- #### main.py: file where the API functions are loaded.
- #### README.md

---

## Requirements

- Have Python 3.x installed on your system.
- Run the following command in the terminal to install the required libraries:

  ```bash
  pip install -r requirements.txt
  ```

- Execute in bash:

  ```bash
  uvicorn main:app --host 0.0.0.0 --port 10000 --reload
  ```

---

## API functions:

**`API Development`**

- def **genre( _`Year`: str_ )**: A year is entered and returns a list with the 5 most sold genres in the corresponding order.

- def **games( _`Year`: str_ )**: Enter a year and return a list of games released in the year.

- def **specs( _`Year`: str_ )**: A year is entered and returns a list with the 5 most frequent specs in the year in the corresponding order.

- def **earlyaccess( _`Year`: str_ )**: Number of games released in a year with early access.

- def **sentiment( _`Year`: str_ )**: According to the year of release, a list is returned with the number of records that are categorized with a sentiment analysis.

- def **metascore( _`Year`: str_ )**: Top 5 games according to year with the highest metascore.

---

## Deployment and Testing

After testing it locally, the project was put into production using the Render web service: [Deploy Here!](https://steam-recommendation-model.onrender.com/)

---
