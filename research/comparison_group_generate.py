import pandas as pd
import csv
import plotly.graph_objects as go
import math
import plotly.express as px

# read data
data = pd.read_csv(r'rotated.csv')

# normalization
lat_mean = data['LAT'].mean()
lat_std = data['LAT'].std()

lon_mean = data['LON'].mean()
lon_std = data['LON'].std()

# SOG_mean = data['SOG'].mean()
# SOG_std = data['SOG'].std()
# COG_mean = data['COG'].mean()
# COG_std = data['COG'].std()

Heading_mean = data['Heading'].mean()
Heading_std = data['Heading'].std()


# clustering
file = open(r'rotated.csv')
reader = csv.DictReader(file)

# set the configurations
# minimum number of neighbours surrounding a point
# to be considered a cluster point
min_pts = 5
# maximum allowable distance for neighbouring points
eps = 0.8

# transformation into points
points = []
for row in reader:
    Latitude = float(row["LAT"])
    Longitude = float(row["LON"])
    # SOG = float(row["SOG"])
    # COG = float(row["COG"])
    Heading = float(row["Heading"])

    # normalization
    Latitude_norm = (Latitude - lat_mean) / lat_std
    Longitude_norm = (Longitude - lon_mean) / lon_std
    # SOG_norm = (SOG - SOG_mean) / SOG_std
    # COG_norm = (COG - COG_mean) / COG_std
    Heading_norm = (Heading - Heading_mean) / Heading_std

    points.append([Latitude_norm, Longitude_norm, Heading_norm, 0, False])

cluster_num = 1
for point in points:
    if point[3] == 0:
        point[3] = cluster_num
        cluster_num += 1
    point[4] = True
    for point_2 in points:
        if point_2[4]:
            continue
        else:
            dis = math.pow(math.pow((point[0] - point_2[0]), 2) + math.pow((point[1] - point_2[1]), 2) + math.pow((point[2] - point_2[2]), 2), 1/2)
            if dis <= eps:
                point_2[3] = point[3]
                point_2[4] = True

cluster_flag = []
for point in points:
    cluster_flag.append(point[3])
data['color'] = cluster_flag

token = "pk.eyJ1IjoieHV5YW5naGFuIiwiYSI6ImNqb292OW91MDBjbnIzd3B1ZjQwMmYwN3AifQ.6X-GpQEWdqQKVX7xn5h5gw"
# you will need your own token

# Visualize the Raw Points
fig = px.scatter_mapbox(data,
                        lat="LAT",
                        lon="LON",
                        hover_name="MMSI",
                        color="color",
                        hover_data=['color', 'Heading'],
                        color_discrete_sequence=cluster_flag,
                        zoom=3,
                        height=800
                        )

fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

