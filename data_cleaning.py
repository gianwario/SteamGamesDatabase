import pandas as pd
import os
from os import path
import re

project_path = os.getcwd()

# Funzione che chiama le funzioni di utilità per la pulizia dei dati
def clean_dataset():
    dataset = pd.read_csv(path.join(project_path, "steam_data.csv"))
    print(f"INITIAL SHAPE: {dataset.shape}")
    print(1)
    dataset = drop_unused_columns(dataset)
    print(2)
    dataset = drop_missing_values(dataset)
    print(3)
    dataset = drop_equals(dataset)
    print(4)
    dataset = modify_reviews(dataset)
    print(5)
    dataset = modify_price(dataset)
    print(6)

    dataset.reset_index(drop=True, inplace=True)
    print(f"ENDING SHAPE: {dataset.shape}")
    modify_pegi(dataset)
    pd.DataFrame(dataset).to_csv(path.join(project_path, "clean_dataset.csv"))

# Funzione che elimina i valori nulli
def drop_missing_values(dataset):

    for row in dataset.iloc():
        for i in range(8):
            if str(row[i]) == '-':
                row[i] = pd.NA

    dataset = dataset.dropna()
    return dataset

# Funzione che elimina colonne non utili
def drop_unused_columns(dataset):
    #Inutli
    dataset = dataset.drop(columns='publisher')
    dataset = dataset.drop(columns='developer')
    #C'è users review
    dataset = dataset.drop(columns='all_reviews')
    #Informattabile
    dataset = dataset.drop(columns='pegi')
    return dataset


# Funzione che elimina righe con lo stesso nome
def drop_equals(dataset):
    dataset = dataset.drop_duplicates(subset = ['name'])
    return dataset

# Funzione che trasforma la colonna "users_reviews" in una coppia di numeri
def modify_reviews(dataset):

    for index, row in dataset.iterrows():
        text = row['user_reviews']
        users = re.search(r'\((.*?)\)', text)
        percentage = re.search(r'- (.*?)%', text)

        if users and percentage:
            users = users.group(1)
            percentage = percentage.group(1)
            new_review = users + ';' + percentage
            dataset.loc[index, 'user_reviews'] = new_review

        else:
            dataset = dataset.drop(index, axis = 0)

    return dataset

def modify_price(dataset):

    for index, row in dataset.iterrows():

        text = row['price']
        price = re.search(r'\$(.*?)Add', text)

        if price:
            price = price.group(1)
            price = re.search(r'([0-9]+[.][0-9]+)', price)
            if price:
                price = price.group(1)
                dataset.loc[index, 'price'] = price
            else:
                dataset = dataset.drop(index, axis=0)

        elif "Free to Play" in row['price']:
                dataset.loc[index, 'price'] = "0.00"

        else:
            dataset = dataset.drop(index, axis=0)

    return dataset

def modify_pegi(dataset):

    tmp = dataset.drop_duplicates(subset = ['pegi_url'])
    print(tmp['pegi_url'])

    return dataset

clean_dataset()
