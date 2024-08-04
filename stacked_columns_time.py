import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

mp.rcParams.update({'font.size': 11}) # must set in top

# Data to be plotted with time (ns) information
data = [
    ["Average\nThread Context\nSwitch\nUsing Yield (SLL)", 2215, 3321, 6638],
    ["Average\nThread Context\nSwitch\nUsing Yield (RBT)", 3486, 5228, 10452],
    ["Average\nThread Context\nSwitch\nUsing Yield (TQM)", 2269, 3402, 6801],
    ["Average\nContext Switch\nTime Between\nThreads (SLL)", 2373, 3559, 7118],
    ["Average\nContext Switch\nTime Between\nThreads(RBT)", 5335, 8002, 16005],
    ["Average\nContext Switch\nTime Between\nThreads (TQM)", 2356, 3534, 7068]
]

# form dataframe from data
df = pd.DataFrame(data, columns=["", 
                                 "CPU 240 Mhz", 
                                 "CPU 160 Mhz",
                                 "CPU 80 Mhz",
                                ])
 
# plot multiple columns such as population and year from dataframe
df.plot(x="", y=["CPU 240 Mhz", "CPU 160 Mhz", "CPU 80 Mhz"],  yticks=np.arange(0, 17005, 2000),
        kind="bar", figsize=(10, 10), rot =0,  color=["#77b41f", "#b41f2d", "#1fb4a7"],width=0.5)
mp.tight_layout()
mp.ylim(0, 17005)
ax = mp.gca()
ax.set_box_aspect(1)



# display plot
mp.show()