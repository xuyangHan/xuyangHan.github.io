import csv
import pandas as pd

csvfile = open(r'new5.csv', 'r')
reader = csv.DictReader(csvfile)

with open('Check_Points.csv', 'w') as file:
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

        if i <= 20:
            writer.writerow(row)
            # file.write(row)

print('Data Loading finished.')
