import pandas as pd
import json
from pymongo import MongoClient

df = pd.read_csv(r'C:\Users')

mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
db = mongo_client.Mexico_Gulf_Data
db.pointData.drop()

i = 1
# df columns
# "MMSI", "BaseDateTime", "LAT", "LON", "SOG", "COG", "Heading",
# "VesselName", "IMO", "CallSign", "VesselType", "Status", "Length", "Width",
# "Draft", "Cargo"
for point in df.values:
    VesselName = point[7]
    if pd.isnull(VesselName):
        Latitude = point[2]
        Longitude = point[3]
        if 18.5 < Latitude < 32.5 and -97.5 < Longitude < -79.5:
            MMSI = point[0]
            BaseDateTime = point[1]
            SOG = point[4]
            COG = point[5]
            Heading = point[6]
            IMO = point[8]
            CallSign = point[9]
            VesselType = point[10]
            Status = point[11]
            Length = point[12]
            Width = point[13]
            Draft = point[14]
            Cargo = point[15]
            d = {
                "MMSI": MMSI,
                "BaseDateTime": BaseDateTime,
                "Location": {
                    "Latitude": Latitude,
                    "Longitude": Longitude
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
            db.pointData.insertOne(d)
    if i % 1000 == 0:
        print(i)
    i = i + 1

