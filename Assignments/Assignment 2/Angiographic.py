from __future__ import print_function
import numpy as np
import matplotlib as mpl
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
boxcarSum = 0.0
sliceData = [] 
sortedArray = []
middleIndex  = 0
intensity, low , medium, heigh = ('Intensity', 'Low', 'Medium', 'Heigh')

# Read and create 2D-array from data in a binary file.
dataSet = np.fromfile("slice150.raw", dtype=np.uint16).reshape(rows, cols)

# Create 1D array for future use.
data = dataSet.flatten()
rmin = min(data)
rmax = max(data)

# Display raw input start.
img1 = plt.imshow(dataSet,aspect='equal', cmap=cm.get_cmap(name='magma'), vmin= rmin, vmax= rmax)
ax1 = plt.gca()
cb1 = plt.colorbar(img1,orientation='vertical', ax=ax1)
cb1.set_label(intensity)
cb1.set_ticks([rmin, (rmax / 2), rmax])
cb1.set_ticklabels([low, medium, heigh])
plt.title('150th slice of a CT angiographic scan data.')
plt.axis('off')
plt.savefig('Slice150.png')
plt.show()
# Display raw input end.

# a) Profile line Start.
plt.plot(dataSet[255],'tab:green')  #Line 256th
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
    for it in li:
        cal = (it - mean)
        varianceSum = varianceSum + (cal * cal)
variance = round((varianceSum / (rows * cols)),2)
print('Variance = ', variance)
# b) Calculate Variance value end.

# c) Histogram start.
plt.hist(data, bins=512, log=True, color='c')
plt.title('Histogram of 2D data set.')
plt.xlabel('x-axis')
plt.ylabel('log scale')
plt.savefig("Histogram.png")
plt.show()
# c) Histogram end.

# d) Linear transformation Start.
for r in range(rows):
    for c in range(cols):
        sLinear[r][c] = int(round(((dataSet[r][c] - rmin) / (rmax - rmin)) * smax))
linear1d = np.asarray(sLinear).flatten()        
minLinear = min(linear1d)
maxLinear = max(linear1d)             
img2 = plt.imshow(sLinear, aspect= 'equal', cmap= cm.get_cmap(name='magma'), vmin= minLinear, vmax= maxLinear)
ax2 = plt.gca()
cb2 = plt.colorbar(img2,orientation='vertical', ax=ax2)
cb2.set_label(intensity)
cb2.set_ticks([minLinear, (maxLinear / 2), maxLinear])
cb2.set_ticklabels([low, medium, heigh])
plt.title('Linear Transformation of 2D Data set in range between 0 to 255.')
plt.axis('off')
plt.savefig('LinearTransformation.png')
plt.show()
# d) Linear transformation End.

# e) Different transformation start.
constant = smax / log(rmax + 1, 2)
for m in range(rows):
    for n in range(cols):
        sNonLinear[m][n] = int(round(constant * (log(dataSet[m][n] + 1, 2))))
nonLinear1d = np.asarray(sNonLinear).flatten()         
minNonLinear = min(nonLinear1d)
maxNonLinear = max(nonLinear1d)        
img3 = plt.imshow(sNonLinear, aspect= 'equal', cmap= cm.get_cmap(name='magma'), vmin= minNonLinear, vmax= maxNonLinear)
ax3 = plt.gca()
cb3 = plt.colorbar(img3, orientation= 'vertical', ax= ax3)
cb3.set_label(intensity)
cb3.set_ticks([minNonLinear, (maxNonLinear / 2), maxNonLinear])
cb3.set_ticklabels([low, medium, heigh])
plt.title('Non-Linear Transformation of 2D Data set in range between 0 to 255.')
plt.axis('off')
plt.savefig('Non-LinearTransformation.png')
plt.show()
# e) Different transformation end.

# f) 11x11 boxcar smoothing filter start.
for ro in range(filterRows):
    for co in range(filterColmns):
        rowEnd = (ro + kernelRows)
        columnEnd = (co + kernelColmns)
        for p in dataSet[ro:rowEnd, co:columnEnd]:
            for q in p:                
                boxcarSum = boxcarSum + ((1 / (kernelRows * kernelColmns)) * q)       
        boxcarSmoothingFilter[ro][co] = int(round(boxcarSum))
        boxcarSum = 0.0
boxcar1d = np.asarray(boxcarSmoothingFilter).flatten()         
minBoxcar = min(boxcar1d)
maxBoxcar = max(boxcar1d)        
img4 = plt.imshow(boxcarSmoothingFilter, aspect= 'equal', cmap= cm.get_cmap(name='magma'), vmin= minBoxcar, vmax= maxBoxcar)
ax4 = plt.gca()
cb4 = plt.colorbar(img4, orientation= 'vertical', ax= ax4)
cb4.set_label(intensity)
cb4.set_ticks([minBoxcar, (maxBoxcar / 2), maxBoxcar])
cb4.set_ticklabels([low, medium, heigh])
plt.title('An 11x11 boxcar smoothing filter on the 2D data set.')
plt.axis('off')
plt.savefig('BoxcarSmoothingFilter.png')
plt.show()
# f) 11x11 boxcar smoothing filter end.

# g) 11x11 median filter start.
def Sort(li):
    for w in range(1,len(li)):
        key = li[w]
        z = w - 1
        while z >= 0 and key < li[z]:
            li[z+1] = li[z]
            z = z - 1
        li[z+1] = key
    return li

for x in range(filterRows):
    for y in range(filterColmns):
        rEnd = (x + kernelRows)
        cEnd = (y + kernelColmns)
        for arrayList in dataSet[x:rEnd, y:cEnd]:
            for item in arrayList:
                sliceData.append(item)
        sortedArray = Sort(sliceData)        
        middleIndex = len(sortedArray) // 2                
        medianFilter[x][y] = int(round(sortedArray[middleIndex]))
        sliceData = []
        sortedArray = []
        middleIndex = 0
Median1d = np.asarray(medianFilter).flatten()
minMedian = min(Median1d)
maxMedian = max(Median1d)
img5 = plt.imshow(medianFilter, aspect= 'equal', cmap= cm.get_cmap(name='magma'), vmin= minMedian, vmax= maxMedian)
ax5 = plt.gca()
cb5 = plt.colorbar(img5, orientation= 'vertical', ax= ax5)
cb5.set_label(intensity)
cb5.set_ticks([minMedian, (maxMedian / 2), maxMedian])
cb5.set_ticklabels([low, medium, heigh])
plt.title('An 11x11 Median filter on the 2D data set.')
plt.axis('off')
plt.savefig('MedianFilter.png')
plt.show()
# g) 11x11 median filter end
