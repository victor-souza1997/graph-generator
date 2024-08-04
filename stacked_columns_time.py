import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

mp.rcParams.update({'font.size': 11})  # must set at the top

# Data to be plotted with time (ns) information
data = [
    ["Average\nThread Context\nSwitch Using\nYield (SLL)", 2215, 3321, 6638],
    ["Average\nThread Context\nSwitch Using\nYield (RBT)", 3486, 5228, 10452],
    ["Average\nThread Context\nSwitch Using\nYield (TQM)", 2269, 3402, 6801],
    ["Average\nContext Switch\nTime Between\nThreads (SLL)", 2373, 3559, 7118],
    ["Average\nContext Switch\nTime Between\nThreads (RBT)", 5335, 8002, 16005],
    ["Average\nContext Switch\nTime Between\nThreads (TQM)", 2356, 3534, 7068]
]

# Form DataFrame from data
df = pd.DataFrame(data, columns=["Benchmark", "CPU 240 MHz", "CPU 160 MHz", "CPU 80 MHz"])

# Plot multiple columns such as context switch times from DataFrame
bar_width = 0.3  # Adjusted bar width
fig, ax = mp.subplots(figsize=(1, 1))  # Adjusted figure size to be more compact and square

bar_positions = np.arange(len(df))  # The positions of the bar groups

bars1 = ax.bar(bar_positions - bar_width, df["CPU 240 MHz"], width=bar_width, label='CPU 240 MHz', color="#77b41f")
bars2 = ax.bar(bar_positions, df["CPU 160 MHz"], width=bar_width, label='CPU 160 MHz', color="#b41f2d")
bars3 = ax.bar(bar_positions + bar_width, df["CPU 80 MHz"], width=bar_width, label='CPU 80 MHz', color="#1fb4a7")

ax.set_xticks(bar_positions)
ax.set_xticklabels(df["Benchmark"], rotation=0)

ax.set_yticks(np.arange(0, 17005, 2000))
ax.set_ylim(0, 17005)

ax.legend()
ax.set_ylabel("Time (ns)")
mp.tight_layout()

# Display plot
mp.show()
