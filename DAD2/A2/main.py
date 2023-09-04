# Reading the file
with open("40.txt", "r") as file:
    content = file.readlines()

# Identifying and extracting the required values
throughput_values = []
signal_delay_values = []

for i in range(len(content)):
    if "Average throughput:" in content[i]:
        throughput_values.append(float(content[i].split()[2]))
    if "95th percentile signal delay:" in content[i]:
        signal_delay_values.append(float(content[i].split()[4]))

# Calculating power for each set of values
powers = [(throughput / delay) * 1000 for throughput, delay in zip(throughput_values, signal_delay_values)]

# Finding the maximum power
max_power = max(powers)

print("Throughput values: ", throughput_values)
print("Signal delay values: ", signal_delay_values)
print("Power values: ", powers)
print("Maximum power: ", max_power)