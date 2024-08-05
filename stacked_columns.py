import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

mp.rcParams.update({'font.size': 15})  # must set in top

# Data to be plotted
data = [
    ["Semaphore\nTake Time\n(SLL)", 720, 720, 720],
    ["Semaphore\nTake Time\n(RBT)", 948, 948, 948],
    ["Semaphore\nTake Time\n(TQM)", 755, 755, 755],
    ["Semaphore\nGive Time\n(SLL)", 1739, 1425, 1112],
    ["Semaphore\nGive Time\n(RBT)", 2067, 1753, 1440],
    ["Semaphore\nGive Time\n(TQM)", 1742, 1428, 1115]
]

# Form dataframe from data
df = pd.DataFrame(data, columns=["", 
                                 "CPU 240 Mhz", 
                                 "CPU 160 Mhz",
                                 "CPU 80 Mhz"])

# Plot multiple columns such as population and year from dataframe
ax = df.plot(x="", y=["CPU 240 Mhz", "CPU 160 Mhz", "CPU 80 Mhz"],
             kind="bar", figsize=(8, 6), rot=0, yticks=np.arange(0, 2200, 100),
             color=["#77b41f", "#b41f2d", "#1fb4a7"], width=0.8)

# Annotate bars with their values
for c in ax.containers:
    ax.bar_label(c, label_type='edge', padding=3)

mp.ylabel("Clock Cycles")
mp.tight_layout()
mp.ylim(0, 2200)
# Display plot
mp.show()