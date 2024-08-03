import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
 
mp.rcParams.update({'font.size': 13})
# data to be plotted
data = [["Switch from ISR \nBack to Interrupted \nThread (Group 1)", 1144, 830, 531],
        ["Switch from ISR \nBack to Interrupted \nThread (Group 2)", 1144, 830, 531],
        ["Switch from ISR \nBack to Interrupted \nThread (Group 3)", 1144, 830, 531],
        ["Time from ISR to \nExecuting a Different \nThread (Group 1)", 451, 451, 451],
        ["Time from ISR to \nExecuting a Different \nThread (Group 2)", 451, 451, 451],
        ["Time from ISR to \nExecuting a Different \nThread (Group 3)", 451, 451, 451]]
 
# form dataframe from data
df = pd.DataFrame(data, columns=["Benchmarks Divided by Group", 
                                 "CPU 240 Mhz", 
                                 "CPU 160 Mhz",
                                 "CPU 80 Mhz",
                                ])
 
# plot multiple columns such as population and year from dataframe
df.plot(x="Benchmarks Divided by Group", y=["CPU 240 Mhz", "CPU 160 Mhz", "CPU 80 Mhz"],
        kind="bar", figsize=(10, 10), rot =0, yticks=np.arange(0, 1200, 50))
mp.ylabel("Clock Cycles")

# display plot
mp.show()