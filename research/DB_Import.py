import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

# CSV to JSON Conversion
csvfile = open(r'C:\Users\62707\Downloads\AIS_ASCII_by_UTM_Month\2017_v2\AIS_2017_01_Zone03.csv', 'r')
reader = csv.DictReader(csvfile)
mongo_client = MongoClient()
db = mongo_client.trajectories_test
db.AIS_2017_01_Zone03.drop()
header = ["MMSI", "BaseDateTime", "LAT", "LON", "SOG", "COG", "Heading",
          "VesselName", "IMO", "CallSign", "VesselType", "Status", "Length", "Width",
          "Draft", "Cargo"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.segment.insert(row)
