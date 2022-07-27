# qui ci mettiamo tutte le query 
from mongo_connection import mongo_connection

# inserimento nuovo gioco
def insert_new_game(date, name, img_url, pegi_desc, price, reviews, tags, url):
    collection = mongo_connection()
    new_game = {'date': date,
                'img_url': img_url,
                'name': name,
                'pegi_desc': pegi_desc,
                'price': float(price),
                'reviews': reviews,
                'tags': tags,
                'url': url}
    collection.insert_one(new_game)

    return list(find_game_by_name(new_game['name']))

# modifica informazioni di un videogioco
def update_game(date, name, img_url, pegi_desc, price, reviews, tags, url):
    collection = mongo_connection()
    new_game = {"$set":{'date': date,
                        'img_url': img_url,
                        'name': name,
                        'pegi_desc': pegi_desc,
                        'price': float(price),
                        'reviews': reviews,
                        'tags': tags,
                        'url': url}}
    collection.update_one({"url":url}, new_game)

    return list(find_game_by_name(name))

# cancellazione di un videogioco
def delete_by_url(url):
    collection = mongo_connection()
    collection.delete_one({"url":url})
    return find_game_by_url(url)


# ricerca per id
def find_game_by_url(search):
    collection = mongo_connection()
    query = collection.find_one({"url":search})
    return query

# ricerca per nome
def find_game_by_name(search):
    collection = mongo_connection()
    query = collection.find({"name" : { '$regex': ".*"+search+".*"}})

    return list(query)

# ricerca per categoria
def find_game_by_category(search):
    collection = mongo_connection()
    query = collection.find({"tags" : search})

    return list(query)

# tutte le possibili ricerche per la recensione (strutturato)
def find_game_by_review_count(search):
    collection = mongo_connection()
    query = collection.find({"reviews.count": {"$gt": int(search)}})

    return list(query)

def find_game_by_review_rating(search):
    collection = mongo_connection()
    query = collection.find({"reviews.value": {"$gt": int(search)}})

    return list(query)

# ordinato per prezzo
def find_game_orderby_price():
    collection = mongo_connection()
    query = collection.find().sort("price", -1)

    return list(query)

# range di prezzo
def find_game_by_price_range(min, max):
    collection = mongo_connection()
    query = collection.find({"price": {"$gt": min, "$lt": max}})

    return list(query)

# ricerca per anno di uscita
def find_game_by_year(year):
    collection = mongo_connection()
    query = collection.find({"date" : { '$regex': ".*"+year+".*"}})

    return list(query)

# ricerca per pegi
def find_game_by_pegi(pegi):
    collection = mongo_connection()
    query = collection.find({"pegi_desc" : pegi})

    return list(query)

# ordinato per rating
def find_game_orderby_rating():
    collection = mongo_connection()
    query = collection.find().sort("reviews.value", -1)

    return list(query)

# consigliare 20 giochi con buon rapporto recensione/prezzo (ordiniamo per #recensioni/valore_recensione e per prezzo)
def find_best_rating_ratio():
    games = find_game_by_name("")
    best_games = []
    ratios = []
    n_limit = 50

    for game in games:

        rating = game['reviews']
        count = int(rating['count'])
        rating = float(rating['value'])
        ratio = float(count / (101 - rating))

        if len(best_games) < n_limit:
            best_games.append(game)
            ratios.append(ratio)

        elif len(best_games) == n_limit:
            min_ratio = min(ratios)
            if ratio > min_ratio:
                min_index = ratios.index(min_ratio)
                ratios.pop(min_index)
                best_games.pop(min_index)
                best_games.append(game)
                ratios.append(ratio)
    new_list = sorted(best_games, key=lambda d: float(d['price']))
    return list(new_list)



