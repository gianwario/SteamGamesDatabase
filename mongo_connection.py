# qui instanziamo la connessione al db di mongo
import pymongo
import pandas as pd

categs = ["Single Player", "Online PvP", "Trading Cards", "MMO", "Single-player", "Online Co-op", "Cross-Platform", "Multiplayer", "In-App Purchases", "Steam Achievements", "Shared/Split Screen", "LAN Co-op", "Remote Play", "Full controller", "Steam Cloud", "Partial Controller"]

# define connection pool
def mongo_connection():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    collection = client["SteamGames"]["SteamGames"]
    return collection


def initialize_db(dataset, collection):
        for index,row in dataset.iterrows():
            categories = row["categories"]
            tags = []
            for c in categs:
                if c in categories:
                    tags.append(c)
            revs = row["user_reviews"]
            revs = revs.split(";")
            element = {
                "_id": index,
                "url": row["url"],
                "name": row["name"],
                "tags": tags,
                "reviews":{
                    "value":revs[0],
                    "count":revs[1]
                },
                "img_url": row["img_url"],
                "date": row["date"],
                "price": row["price"],
                "pegi_desc": row["pegi_desc"],
            }
            collection.insert_one(element)
        return None