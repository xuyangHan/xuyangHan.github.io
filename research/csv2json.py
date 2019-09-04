import json
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv(r'C:\Users\62707\Downloads\data\st lawrence data noaa\st_lawrence_data_bathymetry.csv')

# mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
#                            username='admin',
#                            password='pse212')
mongo_client = MongoClient()
db = mongo_client.Gulf_St_Lawrence_Data
db.bathymetry.drop()

i = 1
for point in df.values:
    try:
        Longitude = float(point[0])
    except ValueError:
        continue

    try:
        Latitude = float(point[1])
    except ValueError:
        continue

    try:
        Depth = float(point[2])
    except ValueError:
        continue

    d = {
        "location": {
            "type": "Point",
            "coordinates": [Longitude, Latitude],
        },
        "Depth": Depth
    }
    db.bathymetry.insert_one(d)
    if i % 1000 == 0:
        print(i)

    i = i + 1

print('Data loading finished. \n')
# print('Geospatial indexing started. ')
#
# db.bathymetry.createIndex({"location": "2dsphere"})
# print('Geospatial indexing finished. ')




