import plotly.express as px
import pandas as pd

vremeto = pd.read_csv("dannite.csv")
vremeto.head()
fig = px.line(vremeto, x="    UNIXTIME", y="Temp", title="Grafikata")
fig.show()