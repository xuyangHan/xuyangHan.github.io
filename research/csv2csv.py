import csv
import pandas as pd

csvfile = open(r'C:\Users\admin\Downloads\data downloaded\AIS_ASCII_by_UTM_Month\2017_v2\AIS_2017_01_Zone18.csv', 'r')
reader = csv.DictReader(csvfile)

with open('new5.csv', 'w') as file:
    fieldnames = ["MMSI", "BaseDateTime", "LAT", "LON", "SOG", "COG", "Heading", "VesselName", "IMO", "CallSign",
                  "VesselType", "Status", "Length",	"Width", "Draft", "Cargo"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    i = 1
    for row in reader:
        if i % 10000 == 0:
            print(i)
        i = i + 1

        try:
            MMSI = int(row["MMSI"])
        except ValueError:
            MMSI = row["MMSI"]

        if MMSI == 316013007:
            writer.writerow(row)
            # file.write(row)

print('Data Loading finished.')
