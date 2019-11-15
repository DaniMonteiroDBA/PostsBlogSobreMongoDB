import pymongo
import pprint

#Criar um client
from pymongo import MongoClient

#conectar no MongoDB
client = MongoClient(STRING DE CONEXÃO COM O MONGODB)

#Criar a variável db
db = client.sample_mflix.movies

cursor_GroupBy_Contagem = db.aggregate([
    {
        '$group': {
            '_id': '$runtime', 
            'contagem': {
                '$sum': 1
            }
        }
    }
])
   
for doc in cursor_GroupBy_Contagem:
    pprint.pprint(doc)
 
