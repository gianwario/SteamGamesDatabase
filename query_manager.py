# qui ci mettiamo tutte le query 
from mongo_connection import mongo_connection
import pprint

# inserimento nuovo gioco

# modifica informazioni di un videogioco

# cancellazione di un videogioco

# ricerca per nome
def find_game_by_name(search):
    print(".*"+search+".*")
    collection = mongo_connection()
    query = collection.find({"name" : { '$regex': ".*"+search+".*"}})
    pprint.pprint(list(query))
    return list(query)

# ricerca per categoria (anche più di una)

# tutte le possibili ricerche per la recensione (strutturato)

# stampa top 20 per recensione in una data categoria

# ricerca ordinata per data

# ricerca ordinata per prezzo

# consigliare 10 giochi con buon rapporto prezzo/recensione (ordiniamo per #recensioni/valore_recensione e per prezzo)