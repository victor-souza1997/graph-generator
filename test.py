import pandas as pd
import matplotlib.pyplot as plt
import re

# Function to parse the file content
def parse_file_content(file_content):
    data = []
    current_option = None
    for line in file_content.split('\n'):
        if line.startswith("==>"):
            parts = line.split('_')
            option = parts[1]
            freq = int(parts[2].replace(".txt <==", ""))
            current_option = option
        elif "Average thread context switch using yield" in line:
            cycles, ns = map(int, re.findall(r'\d+', line))
            yield_cycles = cycles
            yield_ns = ns
        elif "Average context switch time between threads (coop)" in line:
            cycles, ns = map(int, re.findall(r'\d+', line))
            coop_cycles = cycles
            coop_ns = ns
            data.append([f'Option{option}_{freq}MHz', freq, yield_ns, coop_ns])
    return data

# Example file content
file_content = """
==> LatencyTest_Option1_160.txt <==
Timing results: Clock frequency: 160 MHz
Average thread context switch using yield                   :     531 cycles ,     3321 ns
Average context switch time between threads (coop)          :     569 cycles ,     3559 ns
==> LatencyTest_Option1_240.txt <==
Timing results: Clock frequency: 240 MHz
Average thread context switch using yield                   :     531 cycles ,     2215 ns
Average context switch time between threads (coop)          :     569 cycles ,     2373 ns
==> LatencyTest_Option1_80.txt <==
Timing results: Clock frequency: 80 MHz
Average thread context switch using yield                   :     531 cycles ,     6638 ns
Average context switch time between threads (coop)          :     569 cycles ,     7118 ns
==> LatencyTest_Option2_160.txt <==
Timing results: Clock frequency: 160 MHz
Average thread context switch using yield                   :     836 cycles ,     5228 ns
Average context switch time between threads (coop)          :    1280 cycles ,     8002 ns
==> LatencyTest_Option2_240.txt <==
Timing results: Clock frequency: 240 MHz
Average thread context switch using yield                   :     836 cycles ,     3486 ns
Average context switch time between threads (coop)          :    1280 cycles ,     5335 ns
==> LatencyTest_Option2_80.txt <==
Timing results: Clock frequency: 80 MHz
Average thread context switch using yield                   :     836 cycles ,    10452 ns
Average context switch time between threads (coop)          :    1280 cycles ,    16005 ns
==> LatencyTest_Option3_160.txt <==
Timing results: Clock frequency: 160 MHz
Average thread context switch using yield                   :     544 cycles ,     3402 ns
Average context switch time between threads (coop)          :     565 cycles ,     3534 ns
==> LatencyTest_Option3_240.txt <==
Timing results: Clock frequency: 240 MHz
Average thread context switch using yield                   :     544 cycles ,     2269 ns
Average context switch time between threads (coop)          :     565 cycles ,     2356 ns
==> LatencyTest_Option3_80.txt <==
Timing results: Clock frequency: 80 MHz
Average thread context switch using yield                   :     544 cycles ,     6801 ns
Average context switch time between threads (coop)          :     565 cycles ,     7068 ns
"""

data = parse_file_content(file_content)

# Form dataframe from data
df = pd.DataFrame(data, columns=["Test", "Frequency (MHz)", "Yield (ns)", "Coop (ns)"])

# Plot multiple columns such as Yield and Coop from dataframe
df.plot(x="Test", y=["Yield (ns)", "Coop (ns)"], kind="line", figsize=(10, 6), marker='o')

# Set plot labels and title
plt.xlabel('Test')
plt.ylabel('Time (ns)')
plt.title('Latency Test Results')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(loc='best')

# Display plot
plt.show()
