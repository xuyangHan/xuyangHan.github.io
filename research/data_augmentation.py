import csv
import random

rand_arr = []
for x in range(150):
    rand_arr.append(random.randint(1, 39600))

file = open('Testing_Data.csv')
reader = csv.DictReader(file)

with open('noises.csv', 'w') as csvfile:
    fieldnames = ["MMSI", "BaseDateTime", "LAT", "LON", "SOG", "COG", "Heading", "VesselName", "IMO", "CallSign",
                  "VesselType", "Status", "Length", "Width", "Draft", "Cargo"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    i = 1
    for num, row in enumerate(reader):
        if num in rand_arr:
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

            writer.writerow(
                {"MMSI": MMSI, "BaseDateTime": BaseDateTime, "LAT": Latitude + 0.005, "LON": Longitude + 0.005,
                 "SOG": SOG, "COG": COG,
                 "Heading": Heading, "VesselName": VesselName, "IMO": IMO, "CallSign": CallSign,
                 "VesselType": VesselName, "Status": Status, "Length": Length, "Width": Width, "Draft": Draft,
                 "Cargo": Cargo}
            )
            writer.writerow(
                {"MMSI": MMSI, "BaseDateTime": BaseDateTime, "LAT": Latitude - 0.005, "LON": Longitude - 0.005,
                 "SOG": SOG, "COG": COG,
                 "Heading": Heading, "VesselName": VesselName, "IMO": IMO, "CallSign": CallSign,
                 "VesselType": VesselName, "Status": Status, "Length": Length, "Width": Width, "Draft": Draft,
                 "Cargo": Cargo}
            )

    print('Data Loading finished.')
