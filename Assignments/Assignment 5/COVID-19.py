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
