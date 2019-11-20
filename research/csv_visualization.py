token = "pk.eyJ1IjoieHV5YW5naGFuIiwiYSI6ImNqb292OW91MDBjbnIzd3B1ZjQwMmYwN3AifQ.6X-GpQEWdqQKVX7xn5h5gw"  # you will need your own token

import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

data = pd.read_csv("rotated_checkpoints.csv")
data2 = pd.read_csv("shifted_checkpoints2.csv")
check_points = pd.read_csv("Check_Points.csv")
fig = px.scatter_mapbox(data,
                        lat="Latitude",
                        lon="Longitude",
                        hover_name="MMSI",
                        hover_data=['COG', 'SOG', 'Heading'],
                        color_discrete_sequence=["fuchsia"],
                        zoom=3,
                        height=800
                        )
# data_lat = data.Latitude
# data_lon = data.Longitude
# fig.add_trace(go.Scattermapbox(
#     lat=data_lat,
#     lon=data_lon,
#     mode='markers',
#     marker=go.scattermapbox.Marker(
#         size=13,
#         opacity=0.7
#     ),
# ))

check_points_lat = check_points.Latitude
check_points_lon = check_points.Longitude
fig.add_trace(go.Scattermapbox(
    lat=check_points_lat,
    lon=check_points_lon,
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=13,
        color='#002863',
        opacity=1
    ),
))
check_points2_lat = data2.Latitude
check_points2_lon = data2.Longitude
fig.add_trace(go.Scattermapbox(
    lat=check_points2_lat,
    lon=check_points2_lon,
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=9,
        color="fuchsia",
        opacity=0.8
    ),
))

fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
