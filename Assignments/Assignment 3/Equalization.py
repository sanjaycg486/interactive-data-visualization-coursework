from typing import List

import numpy as np
import matplotlib.pyplot as plt
import math

rows, cols = (500, 500)
(smin, smax) = (0, 255)
maximumValueList = [0 for x in range(rows)]
Trans = [[0 for x in range(cols)] for y in range(rows)]
RGB_array = [[[0 for x in range(3)] for y in range(cols)] for z in range(rows)]
print(RGB_array)


# Read the band data from file start.
def read_data_from_file(filepath):
    arr, lineData, removeQuote, splitData = ([], [], [], [])

    with open(filepath, 'r') as f:
        lineData = f.readlines()

    for line in reversed(lineData):
        removeQuote = line.replace('"', "")
        splitData.append(removeQuote.split(","))
        removeQuote = []

    for li in splitData:
        for item in li:
            arr.append((float(item)))
    return arr


band1_1d = read_data_from_file("./orion/i170b1h0_t0.txt")
band1_2d = np.asarray(band1_1d).reshape(rows, cols)
band2_1d = read_data_from_file("./orion/i170b2h0_t0.txt")
band2_2d = np.asarray(band2_1d).reshape(rows, cols)
band3_1d = read_data_from_file("./orion/i170b3h0_t0.txt")
band3_2d = np.asarray(band3_1d).reshape(rows, cols)
band4_1d = read_data_from_file("./orion/i170b4h0_t0.txt")
band4_2d = np.asarray(band4_1d).reshape(rows, cols)
# Read the band data from file end.

# Calculate Max., Min., Mean and Variance value for Band2 start.
maxValue = max(band2_1d)
print("Maximum value = ", maxValue)

minValue = min(band2_1d)
print("Minimum value = ", minValue)

meanValue = np.mean(band2_1d)
print("Mean value = ", meanValue)

varianceValue = np.var(band2_1d)
print("Variance value = ", varianceValue)
# Calculate Max., Min., Mean and Variance value for Band2 End.

# Profile line through the Max. value of band2 data start.
for i in range(rows):
    if max(band2_2d[i]) > max(maximumValueList):
        maximumValueList = []
        maximumValueList = band2_2d[i]
# line = plt.figure(1)
plt.plot(maximumValueList, 'tab:green')
plt.title("Profile line through the line with the maximum value of Band2 2D data set.")
plt.xlabel('x-axis.')
plt.ylabel('y-axis.')
plt.savefig("ProfileLine.png")
plt.show()
# Profile line through the Max. value of band2 data end.

# Display Histogram of band2 Data start.
# hist = plt.figure(2)
r_list, abs_occ_values = np.unique(band2_1d, return_counts=True)
plt.plot(r_list, abs_occ_values)
plt.title('Histogram of band2 data set.')
plt.xlabel('Data values on x-axis.')
plt.ylabel('Absolute Occurrence on y-axis.')
plt.savefig("Histogram.png")
plt.show()
# Display Histogram of band2 Data End.

# Rescale values to range between 0 and 255 using transformation start.
# tra = plt.figure(3)
constant = smax / (math.log(maxValue + 1, 2))
for m in range(rows):
    for n in range(cols):
        Trans[m][n] = (constant * (math.log(band2_2d[m][n] + 1, 2)))
Trans_1d = np.asarray(Trans).flatten()
min_Trans = min(Trans_1d)
max_Trans = max(Trans_1d)
img = plt.imshow(Trans, aspect='equal', cmap='gray', vmin=min_Trans, vmax=max_Trans)
ax = plt.gca()
cb = plt.colorbar(img, orientation='vertical', ax=ax)
cb.set_ticks([min_Trans, max_Trans])
ax.set_xticks([0, 100, 200, 300, 400, 500])
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.xaxis.tick_top()
plt.title('Transformation of band2 2D Data set in range between 0 and 255.')
plt.savefig('Transformation.png')
plt.show()
# Rescale values to range between 0 and 255 using transformation end.


# Histogram equalization on each of the four bands start.                    
def histogram_equalization(oned_band):
    r_values, absolute_values, relative_values, CDF_values, s_values = ([], [], [], [], [])

    r_values, absolute_values = np.unique(oned_band, return_counts=True)
    r_values_length = len(r_values)
    band_1d_length = len(oned_band)

    for i in range(r_values_length):
        relative_values.append((absolute_values[i] / (rows * cols)))
        if i == 0:
            CDF_values.append(relative_values[i])
        else:
            CDF_values.append(CDF_values[i - 1] + relative_values[i])
        s_values.append(CDF_values[i] * smax)

    for p in range(band_1d_length):
        for q in range(r_values_length):
            if oned_band[p] == r_values[q]:
                oned_band[p] = s_values[q]
                break
    return oned_band


hist_equ_band1 = np.asarray(histogram_equalization(band1_1d)).reshape(rows, cols)
plt.imshow(hist_equ_band1, aspect='equal', cmap='gray')
ax = plt.gca()
ax.set_xticks([0, 100, 200, 300, 400, 500])
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.xaxis.tick_top()
plt.title('Histogram equalization of Band1.')
plt.savefig("HistogramEqualization_Band1.png")
plt.show()

hist_equ_band2 = np.asarray(histogram_equalization(band2_1d)).reshape(rows, cols)
plt.imshow(hist_equ_band2, aspect='equal', cmap='gray')
ax = plt.gca()
ax.set_xticks([0, 100, 200, 300, 400, 500])
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.xaxis.tick_top()
plt.title('Histogram equalization of Band2.')
plt.savefig("HistogramEqualization_Band2.png")
plt.show()

hist_equ_band3 = np.asarray(histogram_equalization(band3_1d)).reshape(rows, cols)
plt.imshow(hist_equ_band3, aspect='equal', cmap='gray')
ax = plt.gca()
ax.set_xticks([0, 100, 200, 300, 400, 500])
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.xaxis.tick_top()
plt.title('Histogram equalization of Band3.')
plt.savefig("HistogramEqualization_Band3.png")
plt.show()

hist_equ_band4 = np.asarray(histogram_equalization(band4_1d)).reshape(rows, cols)
plt.imshow(hist_equ_band4, aspect='equal', cmap='gray')
ax = plt.gca()
ax.set_xticks([0, 100, 200, 300, 400, 500])
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.xaxis.tick_top()
plt.title('Histogram equalization of Band4.')
plt.savefig("HistogramEqualization_Band4.png")
plt.show()
# Histogram equalization on each of the four bands end.

# Combine Histo-equalized data set to an RGB-image (b4=r, b3=g, b1=b) start.
for i in range(rows):
    for j in range(cols):
        RGB_array[i][j][0] = hist_equ_band4[i][j]
        RGB_array[i][j][1] = hist_equ_band3[i][j]
        RGB_array[i][j][2] = hist_equ_band1[i][j]
plt.imshow(np.uint8(RGB_array), aspect='equal')
ax = plt.gca()
ax.set_xticks([0, 100, 200, 300, 400, 500])
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.xaxis.tick_top()
plt.title('Combine Histo-equalized data set to an RGB-image.')
plt.savefig("RGB_image.png")
plt.show()
