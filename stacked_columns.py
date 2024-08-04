import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

mp.rcParams.update({'font.size': 13}) # must set in top

# data to be plotted


data = [
    ["Time to\ncreate\n(SLL)", 3160, 2203, 1252],
    ["Time to\ncreate\n(RBT)", 3236, 2279, 1328],
    ["Time to\ncreate\n(TQM)", 3160, 2203, 1252],

    ["Time to\nstart\n(SLL)", 1499, 1187, 873],
    ["Time to\nstart\n(RBT)", 1730, 1417, 1103],
    ["Time to\nstart\n(TQM)", 1502, 1189, 876],

    ["Time to\nsuspend\n(SLL)", 724, 724, 724],
    ["Time to\nsuspend\n(RBT)", 914, 914, 914],
    ["Time to\nsuspend\n(TQM)", 761, 761, 761],

    ["Time to\nresume\n(SLL)", 681, 681, 681],
    ["Time to\nresume\n(RBT)", 889, 889, 889],
    ["Time to\nresume\n(TQM)", 724, 724, 724],
    
    ["Time to\nabort\n(SLL)", 709, 709, 395],
    ["Time to\nabort\n(RBT)", 1021, 709, 1021],
    ["Time to\nabort\n(TQM)", 1022, 710, 396]
]


# form dataframe from data
df = pd.DataFrame(data, columns=["", 
                                 "CPU 240 Mhz", 
                                 "CPU 160 Mhz",
                                 "CPU 80 Mhz",
                                ])
 
# plot multiple columns such as population and year from dataframe
df.plot(x="", y=["CPU 240 Mhz", "CPU 160 Mhz", "CPU 80 Mhz"],
        kind="bar", figsize=(10, 1.8), rot =0, yticks=np.arange(0, 3750, 200),
         color=["#77b41f", "#b41f2d", "#1fb4a7"])
mp.ylabel("Clock Cycles")
mp.tight_layout()
mp.ylim(0, 3400)
# display plot
mp.show()