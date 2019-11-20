import pandas as pd
import plotly.graph_objects as go
import math

csv = pd.read_csv('../static/data/jain.csv', header=None)
x = csv[0]
y = csv[1]
# z = csv[2]

# # Visualize the Raw Points
# fig = go.Figure(
#     data=go.Scatter(
#         x=x,
#         y=y,
#         mode='markers',
#         marker=dict(size=10)
#     )
# )
# fig.show()

# transformation into points
points = []
i = 0
while i < len(csv):
    points.append([x[i], y[i], 0, False])
    i = i + 1


# set the configurations
# minimum number of neighbours surrounding a point
# to be considered a cluster point
min_pts = 2
# maximum allowable distance for neighbouring points
eps = 2.5


cluster_num = 1
for point in points:
    if point[2] == 0:
        point[2] = cluster_num
        cluster_num += 1
    point[3] = True
    for point_2 in points:
        if point_2[3]:
            continue
        else:
            dis = math.pow(math.pow((point[0] - point_2[0]), 2) + math.pow((point[1] - point_2[1]), 2), 1/2)
            if dis <= eps:
                point_2[2] = point[2]
                point_2[3] = True


cluster_flag = []
for point in points:
    cluster_flag.append(point[2])
# Visualize the Raw Points
fig = go.Figure(
    data=go.Scatter(
        x=x,
        y=y,
        mode='markers',
        hovertext=cluster_flag,
        marker=dict(color=cluster_flag, size=10)
    )
)
fig.show()
