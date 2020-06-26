import pandas as pd
import plotly.graph_objects as go
import plotly.offline as off
import os
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash
# Reading the csv data file via Github URL and filtering the data based on the continent 'Europe' start.
data_set_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
covid19_data_frame = pd.read_csv(data_set_url)
covid19_data_frame = covid19_data_frame.loc[
    covid19_data_frame['continent'] == 'Europe']  # Filter out data based on Europe continent.
# print(covid19_data_frame)
# print(covid19_data_frame.columns)  # Gives columns of the data frame
# Reading the csv data file via Github URL and filtering the data based on the continent 'Europe' End.


if not os.path.exists('assignment5_plots'):
    os.mkdir('assignment5_plots')

# Task 1 from the concept paper start.
# Coded by Varun Nandkumar Golani

countries_in_europe = covid19_data_frame['location'].unique().tolist()
# print(len(countries_in_europe))
# fig1 = go.Figure()

# for country in countries_in_europe:
#    date_country_data = covid19_data_frame.loc[
#        covid19_data_frame['location'] == country, ['date']].values.tolist()
#    stringency_index_country_data = covid19_data_frame.loc[
#        covid19_data_frame['location'] == country, ['stringency_index']].values.tolist()
#    date_country_data = [element[0] for element in date_country_data]
#    stringency_index_country_data = [element[0] for element in stringency_index_country_data]
#    fig1.add_trace(go.Scatter(x=date_country_data, y=stringency_index_country_data,
#                              mode='lines', name=country))

# off.plot(fig1, filename='assignment5_plots/task_1_line_graph.html')

# Creating color dictionary by combining different discrete plotly maps
color_list = px.colors.qualitative.Alphabet + px.colors.qualitative.Dark24 + px.colors.qualitative.Dark2
color_dict = {countries_in_europe[index]: color_list[index]
              for index in range(len(countries_in_europe))}
print(color_dict)

fig1 = px.line(covid19_data_frame, x='date', y='stringency_index',
               labels={'date': 'Date', 'stringency_index': 'Government stringency index (0-100)',
                       'location': 'European country', 'total_cases': 'Total confirmed cases',
                       'total_deaths': 'Total deaths', 'new_cases': 'New confirmed cases',
                       'new_deaths': 'New deaths'},
               color='location', color_discrete_map=color_dict,
               hover_data=['total_cases', 'total_deaths', 'new_cases', 'new_deaths'],
               title='Task 1: Line Graphs for Multivariate Data', height=700)

#off.plot(fig1, filename='assignment5_plots/task_1_line_graph.html')
# Task 1 from the concept paper End.


# Task 2 from the concept paper start
# Coded by Lalith Sagar Devagudi

#creating a data frame from the actual europe data frame
recent_deaths_data_frame = pd.DataFrame(columns=['location', 'total_cases', 'total_deaths', 'date', 'population', 'hospital_beds_per_thousand' , 'median_age', 'life_expectancy'])

for country in countries_in_europe:
    recent_data = covid19_data_frame.loc[(covid19_data_frame['location'] == country)
                                                 & pd.notnull(covid19_data_frame['total_deaths']) & pd.notnull(covid19_data_frame['total_cases']),
                                                 ['location', 'total_cases', 'total_deaths', 'date', 'population', 'hospital_beds_per_thousand' , 'median_age', 'life_expectancy']]
    if not recent_data.empty:
        recent_deaths_data_frame = pd.concat([recent_deaths_data_frame, recent_data.iloc[[-1]]])

# adding death rates to the data frame 'recent_deaths_data_frame'
covid19_death_rate= []
for i in range(0, len(recent_deaths_data_frame)):
    covid19_death_rate.append((recent_deaths_data_frame['total_deaths'].iloc[i] / recent_deaths_data_frame['total_cases'].iloc[i]) * 100)

recent_deaths_data_frame['covid19_death_rate'] = covid19_death_rate

recent_deaths_data_frame.fillna(0)


# getting number of countries for color
c = []
for i in range(0, len(countries_in_europe)):
    c.append(i)

# Allocating the countries unique numbers
lookup = dict(zip(countries_in_europe,c))
num = []
for i in recent_deaths_data_frame['location']:
    if i in lookup.keys():
        num.append(lookup[i])

# plotting Parallel Coordinates for the data frame
fig1 = go.Figure(data=
    go.Parcoords(
        line = dict(color =num,
                   colorscale = 'HSV',
                   showscale = False,
                   cmin = 0,
                   cmax = len(countries_in_europe)),
        dimensions = list([
                dict(range = [0,len(countries_in_europe)],
                     tickvals = c ,ticktext = countries_in_europe,
                 label = "countries", values = num),
            dict(range = [0, max(recent_deaths_data_frame['hospital_beds_per_thousand'])],
                 label = "Hospitals beds per 1000", values = recent_deaths_data_frame['hospital_beds_per_thousand']),
            dict(range = [0, max(recent_deaths_data_frame['median_age'])],
                 label = 'Median Age', values = recent_deaths_data_frame['median_age']),
            dict(range = [0, max(recent_deaths_data_frame['population'])],
                 label = 'Population', values = recent_deaths_data_frame['population']),
            dict(range = [0, max(recent_deaths_data_frame['life_expectancy'])],
                 label = 'Life expectency', values = covid19_data_frame['life_expectancy']),
            dict(range=[0, max(recent_deaths_data_frame['covid19_death_rate'])],
                 label='COVID_19 Death rate', values=recent_deaths_data_frame['covid19_death_rate']),
            ])

    ), layout=go.Layout(
            autosize=True,
            height=950,
            hovermode='closest',
            margin=dict(l=170, r=85, t=75)))

# updating margin of the plot
fig1.update_layout(
    title={
        'text': "COVID-19[Task_2]",
        'y':0.99,
        'x':0.2,
        'xanchor': 'center',
        'yanchor': 'top'}, font=dict(
        size=15,
        color="#000000"
    ))


off.plot(fig1, filename='assignment5_plots/task_2_parcoords.html')
#Task 2 from the concept paper end

# Task 3 from the concept paper start
# Coded by Varun Nandkumar Golani

recent_tests_data_frame = pd.DataFrame(columns=['location', 'total_tests', 'date'])
# print(not covid19_data_frame.loc[
#          (covid19_data_frame['location'] == 'Albania') & pd.notnull(covid19_data_frame['total_tests']),
#          ['location', 'date', 'total_tests']].empty)

for country in countries_in_europe:
    country_recent_data = covid19_data_frame.loc[(covid19_data_frame['location'] == country)
                                                 & pd.notnull(covid19_data_frame['total_tests']),
                                                 ['location', 'total_tests', 'date']]
    if not country_recent_data.empty:
        recent_tests_data_frame = pd.concat([recent_tests_data_frame, country_recent_data.iloc[[-1]]])

print(recent_tests_data_frame)
print(recent_tests_data_frame['total_tests'].sum())

fig3 = px.pie(recent_tests_data_frame, values='total_tests', names='location', title='Task 3: Pie Chart'
              , color='location', color_discrete_map=color_dict, hover_data=['date']
              , labels={'location': 'European country', 'date': 'Recent data available date',
                        'total_tests': 'Total tests'})

# ,hovertemplate='European country: %{label} <br>Total tests: %{value}
# </br>Recent data available date: %{customdata}'

fig3.update_traces(textposition='inside', textinfo='percent+label'
                   , hovertemplate='Total tests: %{value} <br>Recent data available date,' +
                                   'European country: %{customdata}</br>')

#off.plot(fig3, filename='assignment5_plots/task_3_pie_chart.html')


app=dash.Dash()
app.layout=html.Div([dcc.Graph(figure=fig1),dcc.Graph(figure=fig3)])
app.run_server(debug=True,use_reloader=False)
# Task 3 from the concept paper end
