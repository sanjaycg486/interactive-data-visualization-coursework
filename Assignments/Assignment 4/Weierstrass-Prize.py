import pandas as pd
import plotly.graph_objs as go

# Reading data from file start.
dataFrame = pd.read_csv('DataWeierstrass.csv', delimiter=';')
# Reading data from file end.

# a) Visualize given data with a scatter plot matrix start.
fig1 = go.Figure(data=go.Splom(
    dimensions=[dict(label='Professor', values=dataFrame['professor']),
                dict(label='Lecture', values=dataFrame['lecture']),
                dict(label='Participants', values=dataFrame['participants']),
                dict(label='Professional expertise', values=dataFrame['professional expertise']),
                dict(label='Motivation', values=dataFrame['motivation']),
                dict(label='Clear presentation', values=dataFrame['clear presentation']),
                dict(label='Overall impression', values=dataFrame['overall impression'])]))
title = "Scatter plot Matrix."
fig1.update_layout(title=title, width=1200, height=1200)
fig1.show()
# a) Visualize given data with a scatter plot matrix end.

# # b) Visualize given data with parallel coordinates start.
fig2 = go.Figure(data=go.Parcoords(
    line=dict(color=dataFrame['clear presentation'],
              colorscale='Electric',
              showscale=True,
              cmin=1,
              cmax=6),
    dimensions=list([
        # dict(range=[1, 44], label='Professor', values=dataFrame['professor'].replace('prof', '')),
        # dict(range=[1, 101], label='Lecture', values=dataFrame['lecture']),
        dict(range=[6, 326], label='Participants', values=dataFrame['participants']),
        dict(range=[1, 2.70], label='Professional expertise', values=dataFrame['professional expertise']),
        dict(range=[1, 3.65], label='Motivation', values=dataFrame['motivation']),
        dict(range=[1, 4.40], label='Clear presentation', values=dataFrame['clear presentation']),
        dict(range=[1, 4.10], label='Overall impression', values=dataFrame['overall impression'])
    ])))
fig2.show()
# b) Visualize given data with parallel coordinates end.
