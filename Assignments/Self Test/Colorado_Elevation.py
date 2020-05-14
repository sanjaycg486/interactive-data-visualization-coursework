"""Written by - Sanjay
idea Reference from - Harshit
"""
from __future__ import print_function
import numpy as np 
from PIL import Image

dataSet = []
#open the file in binary format for reading.
with open('colorado_elev.vit',"rb") as f:
    dataSet = bytearray(f.read())

#Display Dataset
print("***Dataset values Start***")
data = [d for d in dataSet]
#print(data)   #In readable format
print(len(data))
print("***Dataset values End***")

print("***Header Start***")
#Extract and display header data from dataset
header = dataSet[0:268]
#headerValues = [h for h in header]     #In readable format
#print(headerValues)
print(len(header))
print("***Header End***")

print("***Pixel array Start***")
#Extract and display Pixel array from dataset
pixelArray = dataSet[268:]
#pixelArrayValues = [p for p in pixelArray]     #In readable format
print(len(pixelArray))
print("***Pixel array End***")

#Visualize the data set on a 400x400 pixel square
imageData = np.asarray(pixelArray,dtype=np.uint8).reshape(400,400) #Convert the input to an array.
img = Image.fromarray(imageData)
img.save("Colorado_Elevation.jpg","JPEG")
img.show()