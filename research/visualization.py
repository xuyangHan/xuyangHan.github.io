from pymongo import MongoClient
import plotly.graph_objs as go
import plotly.express as px

mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
db = mongo_client.Gulf_St_Lawrence_Data
collection = db.lineData

fig = go.Figure()
for line in collection.find():
    long = []
    lat = []
    for point in line['Location']['coordinates']:
        long.append(point[0])
        lat.append(point[1])
    fig.add_trace(go.Scattergeo(
        locationmode='USA-states',
        lon=long,
        lat=lat,
        hoverinfo='text',
        mode='markers',
        marker=dict(
            size=2,
            color='rgb(255, 0, 0)',
            line=dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        )))

    fig.add_trace(go.Scattergeo(
        locationmode='USA-states',
        lon=long,
        lat=lat,
        hoverinfo='text',
        mode='lines',
        line=dict(
            width=0.5,
            color='red'
        ),
        opacity=0.5
    ))


fig.update_layout(
    title_text='Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend=False,
    geo=go.layout.Geo(
        scope='north america',
        projection_type='azimuthal equal area',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        countrycolor='rgb(204, 204, 204)',
    ),
)

fig.show()
