import csv
import random

rand_arr = []
for x in range(150):
    rand_arr.append(random.randint(1, 39600))

csvfile = open('Check_Points.csv')
reader = csv.DictReader(csvfile)

with open('noises.csv', 'w') as csvfile:
    fieldnames = ["MMSI", "BaseDateTime", "LAT", "LON", "SOG", "COG", "Heading", "VesselName", "IMO", "CallSign",
                  "VesselType", "Status", "Length", "Width", "Draft", "Cargo"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    i = 1
    for num, row in enumerate(reader):
        if num in rand_arr:
            
            writer.writerow(row)

        # try:
        #     Latitude0 = float(row["Latitude"])
        # except ValueError:
        #     continue
        # try:
        #     Longitude0 = float(row["Longitude"])
        # except ValueError:
        #     continue
        #
        # Longitude = -(Latitude0 - 44.21926) + Longitude0
        # Latitude = (Longitude + 79.4606) - 44.21926

        try:
            MMSI = int(row["MMSI"])
        except ValueError:
            MMSI = row["MMSI"]
        # if 43.14480 < Latitude < 44.38381 and -79.96854 < Longitude < -75.88100:
        # if MMSI == 316013007:
        # if i < 125:

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

