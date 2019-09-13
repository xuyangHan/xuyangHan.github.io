import pandas as pd
import json
from pymongo import MongoClient
import csv

csvfile = open(r'C:\Users\admin\Downloads\data downloaded\AIS_ASCII_by_UTM_Month\2017_v2\AIS_2017_01_Zone16.csv')
reader = csv.DictReader(csvfile)

mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
# mongo_client = MongoClient()
db = mongo_client.Lakes_Ontario_Data
# db.pointData.drop()

i = 1
# df columns
# "MMSI", "BaseDateTime", "LAT", "LON", "SOG", "COG", "Heading",
# "VesselName", "IMO", "CallSign", "VesselType", "Status", "Length", "Width",
# "Draft", "Cargo"
for row in reader:
    if i % 10000 == 0:
        print(i)
    i = i + 1

    VesselName = row["VesselName"]
    if pd.isnull(VesselName) or VesselName == '':
        continue

    try:
        Latitude = float(row["LAT"])
    except ValueError:
        continue
    try:
        Longitude = float(row["LON"])
    except ValueError:
        continue

    if 43.14480 < Latitude < 44.38381 and -79.96854 < Longitude < -75.88100:
        try:
            MMSI = int(row["MMSI"])
        except ValueError:
            MMSI = row["MMSI"]

        BaseDateTime = row["BaseDateTime"]
        try:
            SOG = float(row["SOG"])
        except ValueError:
            SOG = row["SOG"]
        try:
            COG = float(row["COG"])
        except ValueError:
            COG = row["COG"]
        try:
            Heading = float(row["Heading"])
        except ValueError:
            Heading = row["Heading"]
        IMO = row["IMO"]
        CallSign = row["CallSign"]
        try:
            VesselType = int(row["VesselType"])
        except ValueError:
            VesselType = row["VesselType"]
        Status = row["Status"]
        try:
            Length = float(row["Length"])
        except ValueError:
            Length = row["Length"]
        try:
            Width = float(row["Width"])
        except ValueError:
            Width = row["Width"]
        Draft = row["Draft"]
        Cargo = row["Cargo"]
        d = {
            "MMSI": MMSI,
            "BaseDateTime": BaseDateTime,
            "Location": {
                "type": "Point",
                "coordinates": [Longitude, Latitude]
            },
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
        db.PointData.insert_one(d)

print('Data Loading finished.')
