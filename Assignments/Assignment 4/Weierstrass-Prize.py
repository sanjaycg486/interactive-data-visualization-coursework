import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
data, professor, lecture, participant, professional, motivation, presentation, impression = ([], [], [], [], [], [], [], [])
# Reading data from file start.
with open('DataWeierstrass.csv', newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=';')
    for row in reader:
        data.append(row)
# print(data)
for item in range(1, len(data)):
    for name in range(1):
        professor.append(data[item][name])
        lecture.append(int(data[item][name + 1][7:10]))
        participant.append(int(data[item][name + 2]))
        professional.append(float(data[item][name + 3]))
        motivation.append(float(data[item][name + 4]))
        presentation.append(float(data[item][name + 5]))
        impression.append(float(data[item][name + 6]))
# print(professor,lecture,participant,professional,motivation,presentation,impression)
# print(len(impression))
# Reading data from file end.

# a) Visualize given data with a scatter plot matrix start.
# dataFrame = pd.DataFrame(data, columns=['Lecture','Participant','professional','motivation','presentation','impression'])
# axes = pd.plotting.scatter_matrix(dataFrame, alpha=0.2)
#
# # plt.tight_layout()
# plt.savefig('ScatterplotMatrix.png')
# plt.show()

# a) Visualize given data with a scatter plot matrix end.
