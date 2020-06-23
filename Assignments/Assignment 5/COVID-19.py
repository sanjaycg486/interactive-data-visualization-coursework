import pandas as pd

# Reading the csv data file via Github URL and filtering the data based on the continent 'Europe'
data_set_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
covid19_data_frame = pd.read_csv(data_set_url)
covid19_data_frame = covid19_data_frame.loc[covid19_data_frame['continent'] == 'Europe']
print(covid19_data_frame)
print(covid19_data_frame.columns) #gives columns of the data frame

