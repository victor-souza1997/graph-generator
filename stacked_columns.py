import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

mp.rcParams.update({'font.size': 15}) # must set in top

# data to be plotted
"""
["Average Semaphore\nSignal Time (Group 1)", 135, 135, 135],
        ["Average Semaphore\nSignal Time (Group 2)", 148, 148, 148],
        ["Average Semaphore\nSignal Time (Group 3)", 135, 135, 135],
        
        ["Average Semaphore\nTest Time (Group 1)", 55, 55, 55],
        ["Average Semaphore\nTest Time (Group 2)", 55, 55, 55],
        ["Average Semaphore\nTest Time (Group 3)", 55, 55, 55],
"""

data = [

        ["Semaphore\nTake Time\n(SSL)", 720, 720, 720],
        ["Semaphore\nTake Time\n(RBT)", 948, 948, 948],
        ["Semaphore\nTake Time\n(TQM)", 755, 755, 755],


        ["Semaphore\nGive Time\n(SLL)", 1739, 1425, 1112],
        ["Semaphore\nGive Time\n(RBT)", 2067, 1440, 1753],
        ["Semaphore\nGive Time\n(TQM)", 1742, 1428, 1115]]
 
# form dataframe from data
df = pd.DataFrame(data, columns=["", 
                                 "CPU 240 Mhz", 
                                 "CPU 160 Mhz",
                                 "CPU 80 Mhz",
                                ])
 

# plot multiple columns such as population and year from dataframe
df.plot(x="", y=["CPU 240 Mhz", "CPU 160 Mhz", "CPU 80 Mhz"],
        kind="bar", figsize=(4, 4), rot =0, yticks=np.arange(0, 2100, 100),
        color=["#77b41f", "#b41f2d", "#1fb4a7"],width=0.8)
mp.ylabel("Clock Cycles")

mp.tight_layout()
mp.ylim(0, 2100)
# display plot
mp.show()