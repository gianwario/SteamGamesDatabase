import pandas as pd
import os
from os import path

project_path = os.getcwd()

# qui ci mettiamo tutte le funzioni utili alla pulizia del dataset
def clean_dataset():
    dataset = pd.read_csv(path.join(project_path, "steam_data.csv"))
    print(dataset.info)
    print("--FUNCTION--")
    dataset = drop_unused_columns(dataset)
    dataset = drop_missing_values(dataset)

    dataset = drop_equals(dataset)
    dataset = drop_invalid_reviews(dataset)
    dataset = modify_reviews(dataset)

    pd.DataFrame(dataset).to_csv(path.join(project_path, "clean_dataset.csv"))

# drop na
def drop_missing_values(dataset):

    for row in dataset.iloc():
        for i in range(10):
            if str(row[i]) == '-':
                row[i] = pd.NA

    dataset = dataset.dropna()
    print(dataset.info)

    return dataset

# drop colonne developer e publisher
def drop_unused_columns(dataset):

    dataset = dataset.drop(columns='publisher')
    dataset = dataset.drop(columns='developer')
    print(dataset.info)
    return dataset

# drop su recensioni senza info
def drop_invalid_reviews(dataset):


    return dataset

# drop nomi di gioco uguali
def drop_equals(dataset):
    return dataset

# lavorare su recensione per renderlo da frase a campo combinato {apprezzamento, numero_recensioni}
def modify_reviews(dataset):
    return dataset

clean_dataset()