from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image
from math import log

rows, cols = (512, 512)
filterRows, filterColmns = (502, 502)
smin, smax = (0, 255)
rmin, rmax = (0, 0)
kernelRows, kernelColmns = (11, 11)
mean, variance = (0.0, 0.0)
meanSum, varianceSum, cal = (0, 0, 0.0) 
linearSum, nonLinearSum = (0, 0)
sLinear = [[0 for x in range(cols)] for y in range(rows)]
sNonLinear = [[0 for x in range(cols)] for y in range(rows)]
boxcarSmoothingFilter = [[0 for x in range(filterColmns)] for y in range(filterRows)]
medianFilter = [[0 for x in range(filterColmns)] for y in range(filterRows)]
boxcarSum, boxcarMul  = (0.0, 0.0)
sliceData, sortedArray = ([], [])

# Read and create 2D-array from data in a binary file.
dataSet = np.fromfile("slice150.raw", dtype=np.uint16).reshape(rows, cols)

# Create 1D array for future use.
data = dataSet.flatten()

# a) Profile line Start.
plt.plot(dataSet[255])  #Line 256th
plt.title("256th Profile line of data set.")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig("ProfileLine.png")
plt.show()
# a) Profile line End.

# b) Calculate Mean value start.
for i in range(len(dataSet)):
    meanSum = meanSum + sum(dataSet[i])
mean = round((meanSum / (rows * cols)),2)
print('Mean = ', mean)
# b) Calculate Mean value end.

# b) Calculate Variance value start.
for li in dataSet:
    for item in li:
        cal = (item - mean)
        varianceSum = varianceSum + (cal * cal)
variance = round((varianceSum / (rows * cols)),2)
print('Variance = ', variance)
# b) Calculate Variance value end.

# c) Histogram start.
plt.hist(data,bins=512,log=True,color='c')
plt.title('Histogram of 2D data set.')
plt.xlabel('x-axis')
plt.ylabel('log scale')
plt.savefig("Histogram.png")
plt.show()
# c) Histogram end.

# d) Linear transformation Start.
rmin = min(data)
rmax = max(data)
for r in range(rows):
    for c in range(cols):
        sLinear[r][c] = int(round(((dataSet[r][c] - rmin) / (rmax - rmin)) * smax))
plt.imshow(sLinear,cmap='gray')
plt.title('Linear Transformation of 2D Data set in range between 0 to 255.')
ax = plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.savefig('LinearTransformation.png')
plt.show()
# d) Linear transformation End.

# e) Different transformation start.
constant = smax / log(rmax + 1, 2)
for m in range(rows):
    for n in range(cols):
        sNonLinear[m][n] = int(round(constant * (log(dataSet[m][n] + 1, 2))))
plt.imshow(sNonLinear,cmap='gray')
plt.title('Non-Linear Transformation of 2D Data set in range between 0 to 255.')
ax = plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.savefig('Non-LinearTransformation.png')
plt.show()
# e) Different transformation end.

# f) 11x11 boxcar smoothing filter start.
for ro in range(filterRows):
    for co in range(filterColmns):
        rowEnd = (ro + kernelRows)
        columnEnd = (co + kernelColmns)
        for arrayList in dataSet[ro:rowEnd, co:columnEnd]:
            for item in arrayList:
                boxcarMul = ((1 / (kernelRows * kernelColmns)) * item)
                boxcarSum = boxcarSum + boxcarMul       
        boxcarSmoothingFilter[ro][co] = int(round(boxcarSum))
        boxcarSum, boxcarMul = (0.0, 0.0)
plt.imshow(boxcarSmoothingFilter,cmap='gray')
plt.title('An 11x11 boxcar smoothing filter on the 2D data set.')
ax = plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.savefig('BoxcarSmoothingFilter.png')
plt.show()
# f) 11x11 boxcar smoothing filter end.

# g) 11x11 median filter start
def BubbleSort(li):
    length = len(li)    
    for i in range(length-1):
        for j in range(0,length-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

for r in range(filterRows):
    for c in range(filterColmns):
        rEnd = (r + kernelRows)
        cEnd = (c + kernelColmns)
        for arrayList in dataSet[r:rEnd, c:cEnd]:
            for item in arrayList:
                sliceData.append(item)
        sortedArray = BubbleSort(sliceData)        
        middleIndex = len(sortedArray) // 2                
        medianFilter[r][c] = int(round(sortedArray[middleIndex]))
        sliceData = [], sortedArray = [], middleItem = 0
plt.imshow(medianFilter,cmap='gray')
plt.title('An 11x11 Median filter on the 2D data set.')
ax = plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.savefig('MedianFilter.png')
plt.show()
# g) 11x11 median filter end
