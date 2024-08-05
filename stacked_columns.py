import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
 
mp.rcParams.update({'font.size': 13})
# data to be plotted
data = [["Switch from ISR\nBack to\nInterrupted\nThread (SLL)", 1144, 830, 531],
        ["Switch from ISR\nBack to\nInterrupted\nThread (RBT)", 1144, 830, 531],
        ["Switch from ISR\nBack to\nInterrupted\nThread (TQM)", 1144, 830, 531],
        ["Time from ISR\nto Executing a\nDifferent\nThread (SLL)", 451, 451, 451],
        ["Time from ISR\nto Executing a\nDifferent\nThread (RBT)", 451, 451, 451],
        ["Time from ISR\nto Executing a\nDifferent\nThread (TQM)", 451, 451, 451]]
 
# form dataframe from data
df = pd.DataFrame(data, columns=["", 
                                 "CPU 240 Mhz", 
                                 "CPU 160 Mhz",
                                 "CPU 80 Mhz",
                                ])
 

# plot multiple columns such as population and year from dataframe
df.plot(x="", y=["CPU 240 Mhz", "CPU 160 Mhz", "CPU 80 Mhz"],
        kind="bar", figsize=(6, 6), rot =0, yticks=np.arange(0, 1200, 100),
        color=["#77b41f", "#b41f2d", "#1fb4a7"],width=0.8)
mp.ylabel("Clock Cycles")

mp.tight_layout()
mp.ylim(0, 1200)
# display plot
mp.show()