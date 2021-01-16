import pandas as pd;
import csv;
import plotly.graph_objects as pg;
data_frame = pd.read_csv("data.csv")
mean = data_frame.groupby("level")["attempt"].mean()
fig = pg.Figure(pg.Bar(
x = mean,
y = ["level 1","level 2","level 3","level 4"],
orientation = 'h'
))
fig.show()