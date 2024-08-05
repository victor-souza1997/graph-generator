import pandas as pd
import matplotlib.pyplot as mp
 
# data to be plotted
data = [["Average thread context \nswitch using \nyield (group 1)", 531, 531, 531],
        ["Average thread context \nswitch using \nyield  (group 2)", 836, 836, 836],
        ["Average thread context \nswitch using \nyield  (group 3)", 544, 544, 544],
        ["Average context switch \ntime between \nthreads (group 1)", 569, 569, 569],
        ["Average context switch \ntime between \nthreads ( group 2)", 836, 836, 836],
        ["Average context switch \ntime between \nthreads ( group 2)", 565, 565, 565]]
 
# form dataframe from data
df = pd.DataFrame(data, columns=["Benchmark", 
                                 "240 Mhz", 
                                 "160 Mhz",
                                 "80 Mhz",
                                ])
 
# plot multiple columns such as population and year from dataframe
ax = df.plot(x="Benchmark", y=["240 Mhz", "160 Mhz", "80 Mhz"],
        kind="bar", figsize=(10, 10), rot =0)

# Annotate bars with their values
for c in ax.containers:
    ax.bar_label(c, label_type='edge', padding=3)


# display plot
mp.show()