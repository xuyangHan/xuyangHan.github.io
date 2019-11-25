import json
import pymongo
import csv
import pandas as pd
from pymongo import MongoClient

csvfile = open(r'Testing_Data.csv')
reader = csv.DictReader(csvfile)

client = pymongo.MongoClient("mongodb+srv://han978:Hxy19940520@cluster0-ziegt.mongodb.net/test?retryWrites=true&w=majority")

# mongo_client = MongoClient()
db = client.testing_data


i = 1
for row in reader:
    VesselName = row["VesselName"]
    Latitude = float(row["LAT"])
    Longitude = float(row["LON"])
    MMSI = int(row["MMSI"])
    BaseDateTime = row["BaseDateTime"]
    SOG = float(row["SOG"])
    COG = float(row["COG"])
    Heading = float(row["Heading"])
    IMO = row["IMO"]
    CallSign = row["CallSign"]

    VesselType = int(row["VesselType"])
    Status = row["Status"]

    Length = float(row["Length"])

    Width = float(row["Width"])

    Draft = row["Draft"]
    Cargo = row["Cargo"]

    point = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [Longitude, Latitude]
        },
        "properties": {
            "MMSI": MMSI,
            "BaseDateTime": BaseDateTime,
            "SOG": SOG,
            "COG": COG,
            "Heading": Heading,
            "Vessel Info": {
                "VesselName": VesselName,
                "IMO": IMO,
                "CallSign": CallSign,
                "VesselType": VesselName,
                "Length": Length,
                "Width": Width
            },
            "Status": Status,
            "Draft": Draft,
            "Cargo": Cargo,
        }
    }
    db.tesing_data.insert_one(point)
    if i % 1000 == 0:
        print(i)

    i = i + 1

print('Data loading finished. \n')
# print('Geospatial indexing started. ')
#
# db.bathymetry.createIndex({"location": "2dsphere"})
# print('Geospatial indexing finished. ')




