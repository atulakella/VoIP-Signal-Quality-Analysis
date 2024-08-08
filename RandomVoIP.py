import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Generate synthetic VoIP signal data
np.random.seed(0)  # For reproducibility

num_samples = 150  # Number of data entries

# Generate synthetic data
data = {
    'Latency (ms)': np.random.normal(50, 10, num_samples),  # Latency in milliseconds
    'Jitter (ms)': np.random.normal(5, 2, num_samples),      # Jitter in milliseconds
    'Packet Loss (%)': np.random.uniform(0, 2, num_samples)  # Packet Loss in percentage
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Simple statistical analysis
def analyze_metrics(df):
    # Descriptive statistics
    stats_summary = df.describe()

    # Correlation matrix
    correlation_matrix = df.corr()

    # Simple regression analysis (impact of jitter and latency on packet loss)
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['Jitter (ms)'], df['Packet Loss (%)'])
    jitter_regression = (slope, intercept)

    slope, intercept, r_value, p_value, std_err = stats.linregress(df['Latency (ms)'], df['Packet Loss (%)'])
    latency_regression = (slope, intercept)

    return stats_summary, correlation_matrix, jitter_regression, latency_regression

# Perform the analysis
stats_summary, correlation_matrix, jitter_regression, latency_regression = analyze_metrics(df)

# Step 3: Visualization
def plot_metrics(df, jitter_regression, latency_regression):
    plt.figure(figsize=(14, 6))

    # Plot Latency vs Packet Loss
    plt.subplot(1, 2, 1)
    plt.scatter(df['Latency (ms)'], df['Packet Loss (%)'], alpha=0.7, label='Data Points')
    plt.plot(df['Latency (ms)'], latency_regression[0] * df['Latency (ms)'] + latency_regression[1], color='red', label='Fit Line')
    plt.xlabel('Latency (ms)')
    plt.ylabel('Packet Loss (%)')
    plt.title('Latency vs Packet Loss')
    plt.legend()

    # Plot Jitter vs Packet Loss
    plt.subplot(1, 2, 2)
    plt.scatter(df['Jitter (ms)'], df['Packet Loss (%)'], alpha=0.7, label='Data Points')
    plt.plot(df['Jitter (ms)'], jitter_regression[0] * df['Jitter (ms)'] + jitter_regression[1], color='red', label='Fit Line')
    plt.xlabel('Jitter (ms)')
    plt.ylabel('Packet Loss (%)')
    plt.title('Jitter vs Packet Loss')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Plot the metrics
plot_metrics(df, jitter_regression, latency_regression)

# Step 4: Generate a brief report
def generate_report(stats_summary, correlation_matrix, jitter_regression, latency_regression):
    report = """
    VoIP Signal Quality Analysis Report

    Descriptive Statistics:
    {}
    
    Correlation Matrix:
    {}
    
    Impact of Jitter on Packet Loss:
    Slope: {:.2f}, Intercept: {:.2f}
    
    Impact of Latency on Packet Loss:
    Slope: {:.2f}, Intercept: {:.2f}
    """.format(stats_summary, correlation_matrix, jitter_regression[0], jitter_regression[1], latency_regression[0], latency_regression[1])

    print(report)

# Generate and print the report
generate_report(stats_summary, correlation_matrix, jitter_regression, latency_regression)
