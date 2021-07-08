import plotly.express as go
import pandas as pd
from fantasy import *

data = loadDataset()
print(data)

fig = go.bar(x = data['Player Name'], y = [data['Touches'], data['Passes Completed']] )
fig.write_html('figure.html')

