# qui ci mettiamo tutte le query 
from mongo_connection import mongo_connection

# inserimento nuovo gioco

# modifica informazioni di un videogioco

# cancellazione di un videogioco

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
    query = collection.find({"reviews.count": {"$gt": search}})
    
    return list(query)

def find_game_by_review_rating(search): 
    collection = mongo_connection()
    query = collection.find({"reviews.value": {"$gt": search}})
    
    return list(query)

# ordinato per prezzo
def find_game_orderby_price(): 
    collection = mongo_connection()
    query = collection.find().sort("price", -1)
    
    return list(query)

# ordinato per rating
def find_game_orderby_rating(): 
    collection = mongo_connection()
    query = collection.find().sort("reviews.value", -1)
    
    return list(query)
# consigliare 10 giochi con buon rapporto prezzo/recensione (ordiniamo per #recensioni/valore_recensione e per prezzo)