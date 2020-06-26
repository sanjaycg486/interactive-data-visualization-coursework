import pandas as pd
# import plotly.graph_objects as go
import plotly.offline as off
import os
import plotly.express as px

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

off.plot(fig1, filename='assignment5_plots/task_1_line_graph.html')
# Task 1 from the concept paper End.

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

off.plot(fig3, filename='assignment5_plots/task_3_pie_chart.html')

# Task 3 from the concept paper end
