import pandas as pd;
import csv;
import plotly.graph_objects as pg;
df = pd.read_csv("data.csv")
s_df = df.loc[df['student_id']== "TRL_xsl"]
m = s_df.groupby("level")["attempt"].mean()
y = ["level 1","level 2","level 3","level 4"]
fig = pg.Figure(pg.Scatter(
x = m,
y = y,
orientation = 'h'
))
fig.show()