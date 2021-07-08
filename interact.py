import plotly.express as go
import pandas as pd
from fantasy import *

data = loadDataset()
print(data)

fig = go.bar(data, x=data['Player Name'], y=[data['Touches'], data['Passes Completed']])
fig.update_layout(legend_title_text='Stats')
fig.update_xaxes(title_text="Player Name")
fig.update_yaxes(title_text="Touches and Passes Completed")

fig.write_html('touches_and_passes.html')

fig = go.bar(data, x=data['Player Name'], y=[data['Assists'], data['Goals']])
fig.update_layout(legend_title_text='Stats')
fig.update_xaxes(title_text="Player Name")
fig.update_yaxes(title_text="Touches and Passes Completed")

fig.write_html('goals_and_assists.html')
