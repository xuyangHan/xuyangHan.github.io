import csv
import pandas as pd

csvfile = open('new4.csv')
reader = csv.DictReader(csvfile)

with open('new5.csv', 'w') as csvfile:
    fieldnames = ["MMSI", "Longitude", "Latitude", "SOG", "COG", "Heading"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    i = 1
    for row in reader:
        if i % 10000 == 0:
            print(i)
        i = i + 1

        try:
            Latitude = float(row["Latitude"])
        except ValueError:
            continue
        try:
            Longitude = float(row["Longitude"])
        except ValueError:
            continue
        try:
            MMSI = int(row["MMSI"])
        except ValueError:
            MMSI = row["MMSI"]
        # if 43.14480 < Latitude < 44.38381 and -79.96854 < Longitude < -75.88100:
        # if MMSI == 316013007:
        if i < 125:
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
            writer.writerow({'MMSI': MMSI, "Longitude": Longitude, "Latitude": Latitude, "SOG": SOG, "COG":COG, "Heading":Heading})


print('Data Loading finished.')
