import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.cm as cm
from math import log

band1_1d, band2_1d, band3_1d, band4_1d = ([],[],[],[])
splitData = []
rows, cols = (500, 500)
(smin, smax) = (0, 255)
maximumValueList = [0 for x in range(rows)]
Trans = [[0 for x in range(cols)] for y in range(rows)]
CDF_band1, CDF_band2, CDF_band3, CDF_band4 = ([],[],[],[])
rlist, absoluteOccurence, probabilityOccurence = ([], [], [])
# print(maximumValueList)
# print(len(maximumValueList))

# Read the band data from file start.
def readDataFromFile(filePath):
    arr, lineData, removeQuote, splitData = ([],[],[],[])

    with open(filePath,'r') as f:
        lineData = f.readlines()

    for line in reversed(lineData):
        removeQuote = line.replace('"',"")
        splitData.append(removeQuote.split(","))
        removeQuote = []

    for li in splitData:
        for item in li:
            arr.append((float(item)))
    return arr

def findAbsoluteOccurenceOfValue(r_arr, oneD_Band):
    result = []
    r_arr_length = len(r_arr)        
    for i in range(r_arr_length):
        result.append(oneD_Band.count(r_arr[i]))
    return result
# with open("./orion/i170b2h0_t0.txt","r") as rf2:
    # lineData = rf2.readlines()
# 
# for line in reversed(lineData):
    # removeQuote = line.replace('"',"")
    # splitData.append(removeQuote.split(","))
    # removeQuote = []
# 
# for li in splitData:
    # for item in li:
        # band2_1d.append((float(item)))
# print(band2_1d)
# print(len(band2_1d))
band1_1d = readDataFromFile("./orion/i170b1h0_t0.txt")
band1_2d = np.asarray(band1_1d).reshape(rows,cols)
band2_1d = readDataFromFile("./orion/i170b2h0_t0.txt")
band2_2d = np.asarray(band2_1d).reshape(rows,cols)
band3_1d = readDataFromFile("./orion/i170b3h0_t0.txt")
band3_2d = np.asarray(band3_1d).reshape(rows,cols)
band4_1d = readDataFromFile("./orion/i170b4h0_t0.txt")
band4_2d = np.asarray(band4_1d).reshape(rows,cols)
# plt.imshow(band1_2d)
# plt.savefig("Band2.png")
# plt.show()
# print(band2_2d)
# print(len(band2_2d))
# Read the band2 data from fle end.

# Calculate Max., Min., Mean and Varience value for Band2 start.
maxValue = max(band2_1d)
print("Maximum value = ", maxValue)
# 
minValue = min(band2_1d)
print("Minimum value = ", minValue)
# 
meanValue = np.mean(band2_1d)
print("Mean value = ", meanValue)
# 
varianceValue = np.var(band2_1d)
print("Varience value = ",varianceValue)
# Calculate Max., Min., Mean and Varience value for Band2 End.

# Profile line through the Max. value of band2 data start.
# for i in range(rows):
    # if max(band2_2d[i]) > max(maximumValueList):
        # maximumValueList = []
        # maximumValueList = band2_2d[i]
# plt.plot(maximumValueList,'tab:green')
# plt.title("Profile line through the line with the maximum value of Band2 2D data set.")
# plt.xlabel('x-axis.')
# plt.ylabel('y-axis.')
# plt.savefig("ProfileLine.png")
# plt.show()
# Profile line through the Max. value of band2 data end.

# Display Histogram of band2 Data start.
# rlist = np.unique(band2_1d)
# plt.plot(rlist,findAbsoluteOccurenceOfValue(rlist, band2_1d))
# plt.title('Histogram of band2 data set.')
# plt.xlabel('Data value on x-axis.')
# plt.ylabel('Count on y-axis.')
# plt.savefig("Histogram.png")
# plt.show()
# Display Histogram of band2 Data End.

# Rescale values to range between 0 and 255 using transformation start.
# constant = smax / log(maxValue + 1, 2)
# for m in range(rows):
    # for n in range(cols):
        # Trans[m][n] = (constant * (log(band2_2d[m][n] + 1, 2)))
# plt.imshow(Trans, aspect= 'equal', cmap='gray')
# plt.title('Transformation of band2 2D Data set in range between 0 to 255.')
# ax1 = plt.gca()
# ax1.xaxis.tick_top()
# plt.savefig('Transformation.png')
# plt.show()
# Rescale values to range between 0 and 255 using transformation end.

# Histogram equalization on each of the four bands start.
def findUniqueValue(oneD_Band):
    result = []
    oneD_Band_length = len(oneD_Band)
    for i in range(oneD_Band_length):
        if(oneD_Band[i] not in result):
            result.append(oneD_Band[i])    
    return result

print(np.unique(band1_1d))
print(len(np.unique(band1_1d)))
print(findUniqueValue(band1_1d))

def findRelativeOccurenceOfValue(x):
    return (x / (rows * cols))

def calculateCDFValue(parr,length):
    CDF = []
    for i in range(length):
        if (i == 0):
            CDF.append(parr[i] * smax)
        else:
            CDF.append(CDF[i-1] + parr[i])
    return CDF

def calculateCDFValueWithSmax(arr):
    result = []
    for i in range(len(arr)):
        result[i].append(round(arr[i] * smax))
    return result

# rlist = findUniqueValue(band2_1d)
# print(len(band2_1d))

            

# Histogram equalization on each of the four bands end.
