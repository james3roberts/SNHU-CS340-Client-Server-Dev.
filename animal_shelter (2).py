import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in Mongodatabase"""

       
     #Initializes MongoClient
    def __init__(self, username, password):
        print("Initializing AnimalShelter object...")
        print(f"Connecting to MongoDB with username '{username}' and password '{password}'...")
        self.client = MongoClient(f'mongodb://{username}:{password}@127.0.0.1:35361')
        print("MongoDB connection successful!")
        self.database = self.client['AAC']

    #Implement create method
    def create(self, data):
        if data is not None:
            return self.database.animals.insert_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    #Implement read method
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
    #Implement a read all method to model the entire database
    def read_all(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("Nothing to read, because data parameter is empty")
    
            
    #implement update method
    def update(self,query, data1):
        #if data is not data1:
        if data1 is not None:
            return self.database.animals.update_one(query,{"$set": data1})

        else:
            raise Exception ("Nothing to update")

            
    #Implement delete method
    def delete(self, query):
        if query is not None:
            return self.database.animals.delete_one(query)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")