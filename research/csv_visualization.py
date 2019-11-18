token = "pk.eyJ1IjoieHV5YW5naGFuIiwiYSI6ImNqb292OW91MDBjbnIzd3B1ZjQwMmYwN3AifQ.6X-GpQEWdqQKVX7xn5h5gw" # you will need your own token

import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

data = pd.read_csv("new2.csv")
fig = px.scatter_mapbox(data,
                        lat="Latitude",
                        lon="Longitude",
                        hover_name="MMSI",
                        hover_data=['COG', 'SOG', 'Heading'],
                        color_discrete_sequence=["fuchsia"],
                        zoom=3,
                        height=800)

fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
