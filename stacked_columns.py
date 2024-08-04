import pandas as pd
import matplotlib.pyplot as mp
 

mp.rcParams.update({'font.size': 13}) # must set in top
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
mp.ylim(0, 3400)
mp.ylabel("Clock Cycles")
mp.tight_layout()
df.plot(x="Benchmark", y=["240 Mhz", "160 Mhz", "80 Mhz"],
        kind="bar", figsize=(10, 1.8), rot =0, yticks=np.arange(0, 3750, 100))

# display plot
mp.show()
