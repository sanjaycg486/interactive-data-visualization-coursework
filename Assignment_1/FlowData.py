from __future__ import print_function
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib as matpl 

dataSet = []
# Read the dataset line by line
with open("./field2.irreg.txt","r") as rf:
    dataSet = rf.readlines()

# Set the dimension.
dim_x, dim_y, dim_z = dataSet[2], dataSet[3], dataSet[4]

# Write the actual data entries to different files.
with open("./data.txt","w") as wf:
    for item in dataSet[6:]:
        wf.writelines(item)

# Fill the individual vector by there values
x, y, z, u, v, w = np.loadtxt("./data.txt",unpack=True)

# Set X-axis and Y-axis
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)
medium = (xmin + xmax) / 2

n = 2
color_array = np.sqrt(((u-n)/2)**2 + ((v-n)/2)**2)

cmap = matpl.cm.jet
norm = matpl.colors.Normalize(vmin=xmin,vmax=xmax) 
fig, ax = plt.subplots()
ax.quiver(x, y, u, v,color_array,scale=20)
# add Colorbar
cbar = plt.colorbar(matpl.cm.ScalarMappable(norm=norm,cmap=cmap),ax=ax)
# Set label to Colorbar
cbar.set_label("Flow Velocity")

cbar.set_ticks([xmin,medium,xmax])
cbar.set_ticklabels(["Low","Medium","High"])
ax.set_aspect('equal')
# Add title to plot
plt.title("Visualization of water flowing through the channel.")
# Add x-axis label
plt.xlabel("X equivalent of Vectors")
# Add y-axis label
plt.ylabel("Y equivalent of Vectors")
# Save the plot in png format
plt.savefig("FlowData.png")
# Display the plot
plt.show()