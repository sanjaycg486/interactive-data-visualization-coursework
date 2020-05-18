from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image
from math import log 

rows, cols = (512, 512)
smin, smax = (0, 255)
sLinear = [[0 for x in range(cols)] for y in range(rows)]
sNonLinear = [[0 for x in range(cols)] for y in range(rows)]

# Read and create 2D-array from data in a binary file.
dataSet = np.fromfile("slice150.raw", dtype=np.uint16).reshape(rows, cols)
# print(dataSet)
# print(len(dataSet))
# print(dataSet.shape) #(512,512) dimension
# plt.imshow(dataSet,cmap=cm.gray)
# plt.savefig('Slice150.png')
# plt.show()

# Create 1D array for future use.
data = dataSet.flatten()
# print(data[255]) #Give single element.
# print(data)
# print(len(data)) # 262144 size.

# img = Image.fromarray(dataSet,mode='')
# img.save('Angiographic.png')
# img.show()


# a) Profile line Start.
# plt.plot(dataSet[255])  #Line 256th
# plt.title("256th Profile line of data set.")
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.savefig("ProfileLine.png")
# plt.show()
# a) Profile line End.

summation = 0
mean = 0.0
cal = 0.0
variance = 0.0

# count = 0
# b) Calculate Mean value start.
for i in range(len(dataSet)):
    summation = summation + sum(dataSet[i])
    # count+= 1
# print(count)
# print(summation)
mean = (summation / (rows * cols))
print('Mean = ' + "{:.2f}".format(mean))
# b) Calculate Mean value end.

# b) Calculate Variance value start.
summation = 0
for li in dataSet:
    for item in li:
        cal = (item - mean)
        summation = summation + (cal * cal)
# print(summation)
variance = (summation / (rows * cols))
print('Variance = ' + "{:.2f}".format(variance))
# b) Calculate Variance value end.

# c) Histogram start.
# plt.hist(data,bins=512,log=True)
# plt.title('Histogram of 2D data set.')
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.savefig("Histogram.png")
# plt.show()
# c) Histogram end.

# d) Linear transformation Start.
rmin = min(data)
rmax = max(data)
print(rmin,rmax)
# for r in range(rows):
    # for c in range(cols):
        # sLinear[r][c] = int(round(((dataSet[r][c] - rmin) / (rmax - rmin)) * smax))        
# print(sLinear)
# print(len(sLinear))
# print(min(sLinear.flatten()))
# pop = np.asarray(sLinear)
# print(min(pop.flatten()),max(pop.flatten())) 
# plt.imshow(sLinear,cmap='gray')
# plt.title('Linear Transformation of 2D Data set in range between 0 to 255.')
# ax = plt.gca()
# ax.xaxis.tick_top()
# plt.savefig('LinearTransformation.png')
# plt.show()
# d) Linear transformation End.

# e) Different transformation start.
for m in range(rows):
    for n in range(cols):
        sNonLinear[m][n] = int(round(log((dataSet[m][n] + 1),2)))
# print(sNonLinear)
print(log(2124,2))
# pop = np.asarray(sNonLinear)
# print(min(pop.flatten()),max(pop.flatten()))
plt.imshow(sNonLinear,cmap='gray')
plt.title('Non-Linear Transformation of 2D Data set in range between 0 to 255.')
ax = plt.gca()
ax.xaxis.tick_top()
plt.savefig('Non-LinearTransformation.png')
plt.show()
# e) Different transformation end.