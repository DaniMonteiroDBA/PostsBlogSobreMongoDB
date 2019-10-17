
#**********************************************
#Para entender este exemplo, acesse 
# http://db4beginners.com/blog/change-stream-no-mongodb/
#**********************************************

#Para acessar o MongoDB com o Python, precisamos importar o módulo pymongo 
import pymongo
 
#Importar a classe MongoClient
from pymongo import MongoClient

#conectar no MongoDB, informando os dados do replicaset
client = MongoClient("r1/localhost:30000,localhost:27052,localhost:27053" )

#Criar a variável db, informando qual é o banco de dados
db = client.blog

#informar a coleção que vamos "monitorar"
col = db.post

#Criar a variável change_stream, que "escutará" as alterações que estão acontecendo na coleção
change_stream = client.watch()

#*******************************************
#se eu quisesse monitorar as alterações no banco de dados poderia usar:
#change_stream = db.watch()

#se eu quisesse monitorar as alterações no replicaset:
#change_stream = client.watch()
#*******************************************

#O cs é um objeto do tipo dicionário, que contém informações sobre a atualização que foi feita
for cs in change_stream:
    #Imprimir na tela as alterações realizadas, elas estão documentadas no objeto cs
    print(cs)
    

