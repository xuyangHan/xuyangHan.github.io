import pandas as pd
import plotly.graph_objects as go
import math
import random


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

random.shuffle(points)
# set the configurations
# minimum number of neighbours surrounding a point
# to be considered a cluster point
min_pts = 2
# maximum allowable distance for neighbouring points
eps = 2.5


cluster_num = 1
print('how many points in total')
print(len(points))
i = 1
for point in points:
    print('No. ')
    print(i)
    i += 1
    clustered_points = []
    if point[2] == 0:
        point[2] = cluster_num
        cluster_num += 1
    point[3] = True
    clustered_points.append(point)
    j = 0
    while j < len(clustered_points):
        point_1 = clustered_points[j]
        j += 1
        for point_2 in points:
            if point_2[3] or point_2 in clustered_points or point_2[2] == cluster_num:
                continue
            else:
                dis = math.pow(math.pow((point_1[0] - point_2[0]), 2) + math.pow((point_1[1] - point_2[1]), 2), 1/2)
                if dis <= eps:
                    point_2[2] = point_1[2]
                    clustered_points.append(point_2)


cluster_flag = []
x_s = []
y_s = []
for point in points:
    cluster_flag.append(point[2])
    x_s.append(point[0])
    y_s.append(point[1])


# Visualize the Raw Points
fig = go.Figure(
    data=go.Scatter(
        x=x_s,
        y=y_s,
        mode='markers',
        hovertext=cluster_flag,
        marker=dict(color=cluster_flag, size=10)
    )
)
fig.show()
