import matplotlib.pyplot as plt
import re

# Function to parse the file content
def parse_file_content(file_content):
    data = {}
    current_option = None
    for line in file_content.split('\n'):
        if line.startswith("==>"):
            parts = line.split('_')
            option = parts[1]
            freq = int(parts[2].replace(".txt <==", ""))
            current_option = option
            if option not in data:
                data[option] = {}
            data[option][freq] = {}
        elif "Average thread context switch using yield" in line:
            cycles, ns = map(int, re.findall(r'\d+', line))
            data[current_option][freq]['yield'] = (cycles, ns)
        elif "Average context switch time between threads (coop)" in line:
            cycles, ns = map(int, re.findall(r'\d+', line))
            data[current_option][freq]['coop'] = (cycles, ns)
    return data

# Function to plot the data
def plot_data(data):
    for option, freqs in data.items():
        frequencies = sorted(freqs.keys())
        yield_ns = [freqs[f]['yield'][1] for f in frequencies]
        coop_ns = [freqs[f]['coop'][1] for f in frequencies]

        plt.figure(figsize=(10, 6))
        plt.plot(frequencies, yield_ns, label='Yield', marker='o')
        plt.plot(frequencies, coop_ns, label='Coop', marker='o')

        plt.title(f'Option {option} Latency Test Results')
        plt.xlabel('Clock Frequency (MHz)')
        plt.ylabel('Time (ns)')
        plt.legend()
        plt.grid(True)
        plt.show()

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
plot_data(data)

