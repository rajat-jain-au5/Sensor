from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://rajatjain852:rajat321@cluster0.drhks7r.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

# read data as dataframe
DATABASE_NAME='Sensor'
COLLECTION_NAME='waferfault'
df=pd.read_csv(r"/home/admin1/Desktop/search/sensor-project/notebooks/wafer.csv")
df=df.drop('Unnamed: 0',axis=1)
# convert data to json
json_record=list(json.loads(df.T.to_json()).values())

# dump data to database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

