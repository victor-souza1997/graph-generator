import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

mp.rcParams.update({'font.size': 8}) # must set in top

# data to be plotted


data = [
    ["Time to create\na thread\n(SLL)", 3160, 2203, 1252],
    ["Time to create\na thread\n(RBT)", 3236, 2279, 1328],
    ["Time to create\na thread\n(TQM)", 3160, 2203, 1252],

    ["Time to start\na thread\n(SLL)", 1499, 1187, 873],
    ["Time to start\na thread\n(RBT)", 1730, 1417, 1103],
    ["Time to start\na thread\n(TQM)", 1502, 1189, 876],

    ["Time to suspend\na thread\n(SLL)", 724, 724, 724],
    ["Time to suspend\na thread\n(RBT)", 914, 914, 914],
    ["Time to suspend\na thread\n(TQM)", 761, 761, 761],

    ["Time to resume\na thread\n(SLL)", 681, 681, 681],
    ["Time to resume\na thread\n(RBT)", 889, 889, 889],
    ["Time to resume\na thread\n(TQM)", 724, 724, 724],
    
    ["Time to abort\na thread\n(SLL)", 709, 709, 395],
    ["Time to abort\na thread\n(RBT)", 1021, 709, 1021],
    ["Time to abort\na thread\n(TQM)", 1022, 710, 396]
]


# form dataframe from data
df = pd.DataFrame(data, columns=["", 
                                 "CPU 240 Mhz", 
                                 "CPU 160 Mhz",
                                 "CPU 80 Mhz",
                                ])
 
# plot multiple columns such as population and year from dataframe
df.plot(x="", y=["CPU 240 Mhz", "CPU 160 Mhz", "CPU 80 Mhz"],
        kind="bar", figsize=(10, 1), rot =0, yticks=np.arange(0, 3750, 200))
mp.ylabel("Clock Cycles")
mp.tight_layout()
# display plot
mp.show()