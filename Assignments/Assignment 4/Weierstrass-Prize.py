import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Reading data from file start.
dataFrame = pd.read_csv('DataWeierstrass.csv', delimiter=';')
professor_id, lecture_id = ([], [])
for i in range(len(dataFrame)):
    professor_id.append(int(dataFrame['professor'][i].replace('prof', '')))
    lecture_id.append(int(dataFrame['lecture'][i].replace('lecture', '')))
new_professor_data = pd.DataFrame({'professor': professor_id})
new_lecture_data = pd.DataFrame({'lecture': lecture_id})
dataFrame.update(new_professor_data)
dataFrame.update(new_lecture_data)
# Reading data from file end.


# a) Visualize given data with a scatter plot matrix start.
fig1 = px.scatter_matrix(dataFrame,
                         dimensions=['lecture', 'participants', 'professional expertise', 'motivation',
                                     'clear presentation', 'overall impression'], color='professor',
                         symbol='professor', opacity=1,
                         labels={'professor': 'Professor Id', 'lecture': 'Lecture Id', 'participants': 'Participants',
                                 'professional expertise': 'Professional Expertise', 'motivation': 'Motivation',
                                 'clear presentation': 'Clear Presentation', 'overall impression': 'Overall Impression'},
                         title='Scatter-plot Matrix of University DataWeierstrass data set.', width=1500, height=1500)
fig1.update_traces(diagonal_visible=False)
fig1.show()
# a) Visualize given data with a scatter plot matrix end.

# b) Visualize given data with parallel coordinates start.
fig2 = go.Figure(data=go.Parcoords(
    dimensions=list([
        dict(label='Professor Id', values=dataFrame['professor']),
        dict(label='Lecture Id', values=dataFrame['lecture']),
        dict(label='Participants', values=dataFrame['participants']),
        dict(label='Professional Expertise', values=dataFrame['professional expertise']),
        dict(label='Motivation', values=dataFrame['motivation']),
        dict(label='Clear Presentation', values=dataFrame['clear presentation']),
        dict(label='Overall Impression', values=dataFrame['overall impression'])]),
    line=dict(color=dataFrame['clear presentation'],
              colorscale='Portland',
              showscale=True,
              cmin=1,
              cmid=3,
              cmax=6)))
fig2.update_layout(title='Parallel co-ordinates Plot of University DataWeierstrass data set.')
fig2.show()
# b) Visualize given data with parallel coordinates end.
