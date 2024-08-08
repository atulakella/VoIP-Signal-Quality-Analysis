import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate synthetic VOIP call data
def generate_voip_data(num_entries=200):
    np.random.seed(42)  # For reproducibility

    # Generate random timestamps
    start_time = datetime(2024, 8, 8, 10, 0, 0)
    timestamps = [start_time + timedelta(seconds=i) for i in range(num_entries)]

    # Generate synthetic data for other columns
    source_ips = ['192.168.1.10'] * num_entries
    destination_ips = ['192.168.1.20'] * num_entries
    packet_sizes = np.random.randint(140, 160, size=num_entries)  # Packet size between 140 and 160 bytes
    jitters = np.random.randint(20, 50, size=num_entries)  # Jitter between 5 and 30 ms
    latencies = np.random.randint(15, 40, size=num_entries)  # Latency between 15 and 40 ms
    packet_losses = np.random.uniform(0, 2, size=num_entries)  # Packet loss between 0% and 1%

    # Create DataFrame
    df = pd.DataFrame({
        'Timestamp': timestamps,
        'Source IP': source_ips,
        'Destination IP': destination_ips,
        'Packet Size (Bytes)': packet_sizes,
        'Jitter (ms)': jitters,
        'Latency (ms)': latencies,
        'Packet Loss (%)': packet_losses
    })

    # Calculate additional metrics
    df['Call Duration (s)'] = 1  # Assuming 1-second duration for simplicity
    df['SNR'] = np.random.uniform(10, 30, size=num_entries)  # Random SNR between 10 and 30 dB

    # Calculate R-factor components
    df['Is'] = 1.5 * df['Packet Loss (%)']
    df['Id'] = df['Jitter (ms)'].apply(lambda x: 0.5 if 30 <= x < 60 else (1 if x >= 60 else 0))
    df['Ie'] = (df['Latency (ms)'] - 150) / 10
    df['R-factor'] = 93.2 - df['Is'] - df['Id'] + df['Ie']

    return df

# Generate the dataset
df = generate_voip_data()

# Optionally, save the dataset to a CSV file
df.to_csv('voip_calls_dataset.csv', index=False)

# Display the first few rows of the dataset
print(df.head())
