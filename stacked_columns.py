import pandas as pd
import matplotlib.pyplot as mp
 
# data to be plotted
data = [["Switch from ISR \nback to interrupted \nthread (group 1)", 1144, 830, 531],
        ["Switch from ISR \nback to interrupted \nthread (group 2)", 1144, 830, 531],
        ["Switch from ISR \nback to interrupted \nthread (group 3)", 1144, 830, 531],
        ["Time from ISR to \nexecuting a different \nthread (group 1)", 451, 451, 451],
        ["Time from ISR to \nexecuting a different \nthread (group 2)", 451, 451, 451],
        ["Time from ISR to \nexecuting a different \nthread (group 3)", 451, 451, 451]]
 
# form dataframe from data
df = pd.DataFrame(data, columns=["Benchmark", 
                                 "240 Mhz", 
                                 "160 Mhz",
                                 "80 Mhz",
                                ])
 
# plot multiple columns such as population and year from dataframe
df.plot(x="Benchmark", y=["240 Mhz", "160 Mhz", "80 Mhz"],
        kind="bar", figsize=(10, 10), rot =0)

# display plot
mp.show()