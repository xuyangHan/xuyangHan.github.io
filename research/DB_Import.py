import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

# CSV to JSON Conversion
csvfile = open(r'C:\Users\admin\Downloads\data downloaded\AIS_ASCII_by_UTM_Month\2017_v2\AIS_2017_01_Zone15.csv', 'r')
reader = csv.DictReader(csvfile)
mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
db = mongo_client.trajectories
db.AIS_2017_01_Zone15.drop()
header = ["MMSI", "BaseDateTime", "LAT", "LON", "SOG", "COG", "Heading",
          "VesselName", "IMO", "CallSign", "VesselType", "Status", "Length", "Width",
          "Draft", "Cargo"]

i = 1
for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.AIS_2017_01_Zone15.insert(row)

    if i % 1000 == 0:
        print(i)

    i = i + 1
