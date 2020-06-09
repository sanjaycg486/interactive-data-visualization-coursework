import pandas as pd
import plotly.graph_objs as go

# Reading data from file start.
dataFrame = pd.read_csv('DataWeierstrass.csv',delimiter=';')
print(dataFrame)
# Reading data from file end.

# a) Visualize given data with a scatter plot matrix start.
fig = go.Figure(data=go.Splom(
    dimensions=[dict(label='Professor', values=dataFrame['professor']),
                dict(label='Lecture', values=dataFrame['lecture']),
                dict(label='Participants', values=dataFrame['participants']),
                dict(label='Professional expertise', values=dataFrame['professional expertise']),
                dict(label='Motivation', values=dataFrame['motivation']),
                dict(label='Clear presentation', values=dataFrame['clear presentation']),
                dict(label='Overall impression', values=dataFrame['overall impression'])]))
title = "Scatter plot Matrix."
fig.update_layout(title=title, width=1200, height=1200)
fig.show()
# a) Visualize given data with a scatter plot matrix end.
