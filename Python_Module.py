from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'Password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31676
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        if username and password:
            self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}')
        
        else: 
            USER = 'aacuser'
            PASS = 'Password'
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        
        self.database = self.client[(DB)]
        self.collection = self.database[(COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            results = list(self.database.animals.find(query))
            return results
        else:
            return list(self.database.animals.find({}))
       
 #Create method to implement the U in CRUD
    def update(self, query, updated_data, multiple=False):
        if query is not None and updated_data is not None:
            if multiple:
                result = self.database.animals.update_many(query, {'$set': updated_data})
            else:
                result = self.database.animals.update_one(query, {'$set': updated_data})
                
            return result.modified_count
        else:
            raise Exception ("Updated data cannot be none")
            
#Create method to implement the D in CRUD
    def delete(self, query, multiple=False):
        if query is not None:
            if multiple:
                result = self.database.animals.delete_many(query)
            else:
                result = self.database.animals.delete_one(query)
                
            return result.deleted_count
        else:
            raise Exception ("Query cannot be none")
        