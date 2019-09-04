import os
import csv

csv_dir = r'C:\Users\62707\Downloads\data\great lakes data noaa'
os.chdir(csv_dir)

with open('combined_data.csv', 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Longitude", "Latitude", "Depth"])

    with open('data1.csv', 'r', newline='') as incsv:
        reader = csv.reader(incsv)
        writer.writerows(row for row in reader)

    with open('data2.csv', 'r', newline='') as incsv:
        reader = csv.reader(incsv)
        writer.writerows(row for row in reader)

    with open('data3.csv', 'r', newline='') as incsv:
        reader = csv.reader(incsv)
        writer.writerows(row for row in reader)

    with open('data4.csv', 'r', newline='') as incsv:
        reader = csv.reader(incsv)
        writer.writerows(row for row in reader)
