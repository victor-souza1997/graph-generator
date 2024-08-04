import pandas as pd
import matplotlib.pyplot as mp

# Data to be plotted with time (ns) information
data = [
    ["Average thread context\nswitch using yield\n(Group 1)", 2215, 3321, 6638],
    ["Average thread context\nswitch using yield\n(Group 2)", 3486, 5228, 10452],
    ["Average thread context\nswitch using yield\n(Group 3)", 2269, 3402, 6801],
    ["Average context switch\ntime between threads\n(Group 1)", 2373, 3559, 7118],
    ["Average context switch\ntime between threads\n(Group 2)", 5335, 8002, 16005],
    ["Average context switch\ntime between threads\n(Group 3)", 2356, 3534, 7068]
]

# Form DataFrame from data
df = pd.DataFrame(data, columns=["Benchmark", 
                                 "240 MHz", 
                                 "160 MHz",
                                 "80 MHz"])

# Plot multiple columns such as context switch times from DataFrame
df.plot(x="Benchmark", y=["240 MHz", "160 MHz", "80 MHz"],
        kind="bar", figsize=(10, 2), rot=0)

# Display plot
mp.ylabel("Time (ns)")
mp.tight_layout()

# Display plot
mp.show()
