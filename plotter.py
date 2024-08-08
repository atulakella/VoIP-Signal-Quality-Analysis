import pandas as pd
import matplotlib.pyplot as plt

# File path to the dataset
file_path = r'W:\Projects\CommTech\voip_calls_dataset.csv'

# Load the dataset
df = pd.read_csv(file_path, parse_dates=['Timestamp'])

# Plotting

# Create a figure with subplots
plt.figure(figsize=(15, 10))

# Plot 1: Time vs Jitter
plt.subplot(3, 1, 1)
plt.plot(df['Timestamp'], df['Jitter (ms)'], marker='o', linestyle='-', color='b')
plt.xlabel('Time')
plt.ylabel('Jitter (ms)')
plt.title('Time vs Jitter')
plt.grid(True)

# Plot 2: Time vs Packet Loss
plt.subplot(3, 1, 2)
plt.plot(df['Timestamp'], df['Packet Loss (%)'], marker='o', linestyle='-', color='r')
plt.xlabel('Time')
plt.ylabel('Packet Loss (%)')
plt.title('Time vs Packet Loss')
plt.grid(True)

# Plot 3: Time vs Latency
plt.subplot(3, 1, 3)
plt.plot(df['Timestamp'], df['Latency (ms)'], marker='o', linestyle='-', color='g')
plt.xlabel('Time')
plt.ylabel('Latency (ms)')
plt.title('Time vs Latency')
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
