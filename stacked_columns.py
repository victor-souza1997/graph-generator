import pandas as pd
import matplotlib.pyplot as mp
 
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

        ["Semaphore Take\nTime (Group 1)", 720, 720, 720],
        ["Semaphore Take\nTime (Group 2)", 948, 948, 948],
        ["Semaphore Take\nTime (Group 3)", 755, 755, 755],


        ["Semaphore Give\nTime (Group 1)", 1739, 1425, 1112],
        ["Semaphore Give\nTime (Group 2)", 2067, 1440, 1753],
        ["Semaphore Give\nTime (Group 3)", 1742, 1428, 1115]]
 
# form dataframe from data
df = pd.DataFrame(data, columns=["Benchmark", 
                                 "240 Mhz", 
                                 "160 Mhz",
                                 "80 Mhz",
                                ])
 
# plot multiple columns such as population and year from dataframe
df.plot(x="Benchmark", y=["240 Mhz", "160 Mhz", "80 Mhz"],
        kind="bar", figsize=(10, 10), rot =0)

# display plot
mp.show()