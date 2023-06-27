# Get the database using the method we defined in pymongo_test_insert file
import os
from dotenv import load_dotenv
# helper to use mongoDB ObjectId
from bson.objectid import ObjectId

from src.database import mongoDbConnection
from src.models.k9 import K9

load_dotenv()

dbname = mongoDbConnection.get_database()
# Retrieve a collection named with K9S_COLLECTION .env value from database
COLLECTION = os.getenv('K9S_COLLECTION')
collection_name = dbname[COLLECTION]
   
def find_k9_by_name(k9_name) -> K9:
   dog = collection_name.find_one({"k9_name": k9_name})
   return dog
 
def find_all_k9s() -> list[K9]:
  return collection_name.find()
 
def insert_k9(k9):
  return collection_name.insert_one(k9.__dict__)

def update_k9(_id, k9):
  return collection_name.find_one_and_update({'_id': ObjectId(_id)}, {'$set': {'nature': k9.nature}})

def delete_k9(_id) -> K9:
  return collection_name.find_one_and_delete({'_id': ObjectId(_id)})