import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.cm as cm
from math import log
from collections import Counter

rows, cols = (500, 500)
(smin, smax) = (0, 255)
maximumValueList = [0 for x in range(rows)]
Trans = [[0 for x in range(cols)] for y in range(rows)]

# Read the band data from file start.
def read_Data_From_File(filePath):
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

band1_1d = read_Data_From_File("./orion/i170b1h0_t0.txt")
band1_2d = np.asarray(band1_1d).reshape(rows,cols)
band2_1d = read_Data_From_File("./orion/i170b2h0_t0.txt")
band2_2d = np.asarray(band2_1d).reshape(rows,cols)
band3_1d = read_Data_From_File("./orion/i170b3h0_t0.txt")
band3_2d = np.asarray(band3_1d).reshape(rows,cols)
band4_1d = read_Data_From_File("./orion/i170b4h0_t0.txt")
band4_2d = np.asarray(band4_1d).reshape(rows,cols)
# Read the band data from file end.

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
# data = Counter(band2_1d)
# plt.plot(list(data.keys()),list(data.values()))
# plt.title('Histogram of band2 data set.')
# plt.xlabel('Data values on x-axis.')
# plt.ylabel('Absolute Occurences on y-axis.')
# plt.savefig("Histogram.png")
# plt.show()
# Display Histogram of band2 Data End.

# Rescale values to range between 0 and 255 using transformation start.
# constant = smax / (log(maxValue + 1, 2))
# for m in range(rows):
    # for n in range(cols):
        # Trans[m][n] = (constant * (log(band2_2d[m][n] + 1, 2)))
# Trans_1d = np.asarray(Trans).flatten()
# min_Trans = min(Trans_1d)
# max_Trans = max(Trans_1d)
# img = plt.imshow(Trans, aspect= 'equal', cmap= cm.get_cmap(name='magma'), vmin= min_Trans, vmax= max_Trans)
# ax = plt.gca()
# ax.xaxis.tick_top()
# cb = plt.colorbar(img, orientation= 'vertical', ax= ax)
# cb.set_ticks([min_Trans, max_Trans])
# plt.title('Transformation of band2 2D Data set in range between 0 and 255.')
# plt.savefig('Transformation.png')
# plt.show()
# Rescale values to range between 0 and 255 using transformation end.

# Histogram equalization on each of the four bands start.
def find_Unique_Value(oneD_Band):    
    result = []
    oneD_Band_length = len(oneD_Band)
    for i in range(oneD_Band_length):
        if(oneD_Band[i] not in result):
            result.append(oneD_Band[i])    
    return result

def find_Absolute_Occurence_OfValue(r_arr, oneD_Band):
    result = []
    r_arr_length = len(r_arr)        
    for i in range(r_arr_length):
        result.append(oneD_Band.count(r_arr[i]))
    return result

def find_Relative_Occurence_OfValue(abs_arr):
    result = []
    abs_arr_length = len(abs_arr)
    for i in range(abs_arr_length):
        result.append((abs_arr[i] / (rows * cols)))
    return result

def calculate_CDF_Value(rel_arr):
    result = []
    rel_arr_length = len(rel_arr)
    for i in range(rel_arr_length):
        if (i == 0):
            result.append(rel_arr[i])
        else:
            result.append(result[i-1] + rel_arr[i])
    return result

def calculate_S_Value_WithSmax(cdf_arr):
    result = []
    cdf_arr_length = len(cdf_arr)
    for i in range(cdf_arr_length):
        result.append(int(round(cdf_arr[i] * smax)))
    return result

def HistogramEqualization(band_1d):
    result, r_values, absolute_values, relative_values, CDF_values, s_values = ([], [], [], [], [], [])    
    
    result = Counter(band_1d)
    r_values = list(result.keys())
    absolute_values = list(result.values())
    
    absolute_values_length = len(absolute_values)
    for i in range(absolute_values_length):
        relative_values.append((absolute_values[i] / (rows * cols)))
        if i == 0:            
            CDF_values.append(relative_values[i])
        else:
            CDF_values.append(CDF_values[i-1] + relative_values[i])
        s_values.append(CDF_values[i] * smax)
    
    print('Replacing start')
    band_1d_length = len(band_1d)
    for j, item in enumerate(r_values):
        for k in range(band_1d_length):
            if item == band_1d[k]:
                band_1d[k] = s_values[j]
    print(band_1d)
    return band_1d

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

# r_band1 = find_Unique_Value(band1_1d)
# absoluteOccurence_band1 = find_Absolute_Occurence_OfValue(r_band1, band1_1d)
# relativeOccurence_band1 = find_Relative_Occurence_OfValue(absoluteOccurence_band1)
# CDF_band1 = calculate_CDF_Value(relativeOccurence_band1)
# s_band1 = calculate_S_Value_WithSmax(CDF_band1)
hist_equ_band1 = np.asarray(HistogramEqualization(band2_1d)).reshape(rows, cols)
ax1.imshow(hist_equ_band1, aspect= 'equal')
ax1.set_title('Band1.')
ax1.axis('off')
print('band1')
plt.savefig("HistogramEqualization.png")
plt.show()
# 
# r_band2 = find_Unique_Value(band2_1d)
# absoluteOccurence_band2 = find_Absolute_Occurence_OfValue(r_band2, band2_1d)
# relativeOccurence_band2 = find_Relative_Occurence_OfValue(absoluteOccurence_band2)
# CDF_band2 = calculate_CDF_Value(relativeOccurence_band2)
# s_band2 = calculate_S_Value_WithSmax(CDF_band2)
# hist_equ_band2 = np.asarray(HistogramEqualization(r_band2, s_band2, band2_1d)).reshape(rows,cols)
# ax2.imshow(hist_equ_band2, aspect= 'equal', cmap= cm.get_cmap(name='gray'))
# ax2.set_title('Histogram Equalization of Band2.')
# ax2.axis('off')
# print('band2')
# 
# r_band3 = find_Unique_Value(band3_1d)
# absoluteOccurence_band3 = find_Absolute_Occurence_OfValue(r_band3, band3_1d)
# relativeOccurence_band3 = find_Relative_Occurence_OfValue(absoluteOccurence_band3)
# CDF_band3 = calculate_CDF_Value(relativeOccurence_band3)
# s_band3 = calculate_S_Value_WithSmax(CDF_band3)
# hist_equ_band3 = np.asarray(HistogramEqualization(r_band3, s_band3, band3_1d)).reshape(rows,cols)
# ax3.imshow(hist_equ_band3, aspect= 'equal', cmap= cm.get_cmap(name='gray'))
# ax3.set_title('Histogram Equalization of Band3.')
# ax3.axis('off')
# print('band3')
# 
# r_band4 = find_Unique_Value(band4_1d)
# absoluteOccurence_band4 = find_Absolute_Occurence_OfValue(r_band4, band4_1d)
# relativeOccurence_band4 = find_Relative_Occurence_OfValue(absoluteOccurence_band4)
# CDF_band4 = calculate_CDF_Value(relativeOccurence_band4)
# s_band4 = calculate_S_Value_WithSmax(CDF_band4)
# hist_equ_band4 = np.asarray(HistogramEqualization(r_band4, s_band4, band4_1d)).reshape(rows,cols)
# ax4.imshow(hist_equ_band4, aspect= 'equal', cmap= cm.get_cmap(name='gray'))
# ax4.set_title('Histogram Equalization of Band4.')
# ax4.axis('off')
# print('band4')
# 
# plt.savefig("HistogramEqualization.png")
# plt.show()
# Histogram equalization on each of the four bands end.
