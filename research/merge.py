import os
import csv

csv_dir = r'C:\Users\admin\Downloads\data downloaded'
os.chdir(csv_dir)

with open('combined_data.csv', 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Longitude", "Latitude", "Depth"])

    with open('bathymetric data 1.csv', 'r', newline='') as incsv:
        reader = csv.reader(incsv)
        writer.writerows(row for row in reader)

    with open('bathymetric data 2.csv', 'r', newline='') as incsv:
        reader = csv.reader(incsv)
        writer.writerows(row for row in reader)

