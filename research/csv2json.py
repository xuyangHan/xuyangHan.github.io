import json
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv(r'C:\Users\62707\OneDrive - York University\data\mexico_gulf_bathymetry_data.csv')

mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
db = mongo_client.Mexico_Gulf_Data
db.bathymetry.drop()

i = 1
for point in df.values:
    Longitude = point[0]
    Latitude = point[1]
    Depth = point[2]

    d = {"location": {"Latituded": Latitude, "Longitude": Longitude}, "Depth": Depth}
    db.bathymetry.insert(d)
    if i % 1000 == 0:
        print(i)

    i = i + 1


