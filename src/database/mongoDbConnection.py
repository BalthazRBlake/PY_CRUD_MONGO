import os
from pymongo import MongoClient
from dotenv import load_dotenv

#dotenv will read secret configuration vars from a .env file
load_dotenv()

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING')
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   DATA_BASE = os.getenv('DATA_BASE')
   return client[DATA_BASE]
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()