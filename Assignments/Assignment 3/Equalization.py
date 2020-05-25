import numpy as np

band2_1d = []
splitData = []
rows, cols = (500, 500)

# Read the band2 data line by line
with open("./orion/i170b2h0_t0.txt","r") as rf2:
    lineData = rf2.readlines()

for i in range(len(lineData)):
    removeQuote = lineData[i].replace('"',"")
    splitData.append(removeQuote.split(","))
    removeQuote = []

for li in splitData:
    for item in li:
        band2_1d.append(float(item))
# print(band2_1d)
# print(len(band2_1d))
band2_2d = np.asarray(band2_1d).reshape(rows,cols)
# print(band2_2d)
# print(len(band2_2d))

# Calculate Max., Min., Mean and Varience value for Band2 start.
maxValue = max(band2_1d)
print("Maximum value = ", round(maxValue,2))

minValue = min(band2_1d)
print("Minimum value = ", round(minValue,2))

meanValue = np.mean(band2_1d)
print("Mean value = ", round(meanValue,2))

varianceValue = np.var(band2_1d)
print("Varience value = ", round(varianceValue,2))
# Calculate Max., Min., Mean and Varience value for Band2 End.
