import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

professor_id, lecture_id = ([], [])
# Reading data from file start.
dataFrame = pd.read_csv('DataWeierstrass.csv', delimiter=';')
# print(len(dataFrame))
for i in range(len(dataFrame)):
    professor_id.append(int(dataFrame['professor'][i].replace('prof', '')))
    lecture_id.append(int(dataFrame['lecture'][i].replace('lecture', '')))
new_professor_data = pd.DataFrame({'professor': professor_id})
new_lecture_data = pd.DataFrame({'lecture': lecture_id})
dataFrame.update(new_professor_data)
dataFrame.update(new_lecture_data)
# print(dataFrame)
# Reading data from file end.


# a) Visualize given data with a scatter plot matrix start.
fig1 = px.scatter_matrix(dataFrame,
                         dimensions=['lecture', 'participants', 'professional expertise', 'motivation', 'clear presentation', 'overall impression'],
                         color='professor', symbol='professor', opacity=1,
                         labels={'professor': 'Professor Id', 'lecture': 'Lecture Id', 'participants': 'Participants',
                                 'professional expertise': 'Professional Expertise', 'motivation': 'Motivation',
                                 'clear presentation': 'Clear Presentation', 'overall impression': 'Overall Impression'},
                         title='Scatter plot Matrix of University DataWeierstrass data set.', width=1500, height=1500)
fig1.update_traces(diagonal_visible=False)
fig1.show()
# a) Visualize given data with a scatter plot matrix end.

# # b) Visualize given data with parallel coordinates start.
# fig2 = go.Figure(data=go.Parcoords(
#     line=dict(color=dataFrame['clear presentation'],
#               colorscale='Electric',
#               showscale=True,
#               cmin=1,
#               cmax=6),
#     dimensions=list([
#         # dict(range=[1, 44], label='Professor', values=dataFrame['professor'].replace('prof', '')),
#         # dict(range=[1, 101], label='Lecture', values=dataFrame['lecture']),
#         dict(range=[6, 326], label='Participants', values=dataFrame['participants']),
#         dict(range=[1, 2.70], label='Professional expertise', values=dataFrame['professional expertise']),
#         dict(range=[1, 3.65], label='Motivation', values=dataFrame['motivation']),
#         dict(range=[1, 4.40], label='Clear presentation', values=dataFrame['clear presentation']),
#         dict(range=[1, 4.10], label='Overall impression', values=dataFrame['overall impression'])
#     ])))
# fig2.show()
# b) Visualize given data with parallel coordinates end.
