import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# File path to the dataset
file_path = r'W:\Projects\CommTech\voip_calls_dataset.csv'

# Load the dataset
df = pd.read_csv(file_path, parse_dates=['Timestamp'])

# Perform the analysis
def analyze_metrics(df):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include='number')

    # Descriptive statistics
    stats_summary = numeric_df.describe()

    # Correlation matrix
    correlation_matrix = numeric_df.corr()

    # Simple regression analysis (impact of jitter and latency on packet loss)
    if 'Jitter (ms)' in numeric_df.columns and 'Packet Loss (%)' in numeric_df.columns:
        jitter_slope, jitter_intercept, jitter_r_value, jitter_p_value, jitter_std_err = stats.linregress(numeric_df['Jitter (ms)'], numeric_df['Packet Loss (%)'])
        jitter_regression = (jitter_slope, jitter_intercept)
    else:
        jitter_regression = (None, None)
    
    if 'Latency (ms)' in numeric_df.columns and 'Packet Loss (%)' in numeric_df.columns:
        latency_slope, latency_intercept, latency_r_value, latency_p_value, latency_std_err = stats.linregress(numeric_df['Latency (ms)'], numeric_df['Packet Loss (%)'])
        latency_regression = (latency_slope, latency_intercept)
    else:
        latency_regression = (None, None)

    return stats_summary, correlation_matrix, jitter_regression, latency_regression

# Perform the analysis
stats_summary, correlation_matrix, jitter_regression, latency_regression = analyze_metrics(df)

# Print the statistics and correlation matrix
def print_report(stats_summary, correlation_matrix, jitter_regression, latency_regression):
    print("VoIP Signal Quality Analysis Report\n")
    
    print("Descriptive Statistics:")
    print(stats_summary)
    print("\nCorrelation Matrix:")
    print(correlation_matrix)
    
    if jitter_regression[0] is not None and jitter_regression[1] is not None:
        print("\nImpact of Jitter on Packet Loss:")
        print(f"Slope: {jitter_regression[0]:.2f}, Intercept: {jitter_regression[1]:.2f}")
    
    if latency_regression[0] is not None and latency_regression[1] is not None:
        print("\nImpact of Latency on Packet Loss:")
        print(f"Slope: {latency_regression[0]:.2f}, Intercept: {latency_regression[1]:.2f}")

# Generate and print the report
print_report(stats_summary, correlation_matrix, jitter_regression, latency_regression)

# Plotting
def plot_metrics(df):
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

    plt.tight_layout()
    plt.show()

# Plot the metrics
plot_metrics(df)
