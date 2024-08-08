import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# File path to the dataset
file_path = r'W:\Projects\CommTech\voip_calls_dataset.csv'

# Load the dataset
df = pd.read_csv(file_path, parse_dates=['Timestamp'])

# Print column names to verify
print("Column names in the dataset:")
print(df.columns)

# Define satisfaction levels based on R-Factor
def get_satisfaction_level(r_factor):
    if pd.isna(r_factor):
        return 'Unknown'
    if r_factor >= 93:
        return 'Maximum using G.711'
    elif 90 <= r_factor < 93:
        return 'Excellent'
    elif 80 <= r_factor < 90:
        return 'Good'
    elif 70 <= r_factor < 80:
        return 'Satisfied'
    elif 60 <= r_factor < 70:
        return 'Dissatisfied'
    elif 50 <= r_factor < 60:
        return 'Fully dissatisfied'
    else:
        return 'Not recommended'

# Correct column name for R-Factor
r_factor_column = 'R-factor'

# Print unique R-Factor values to debug
if r_factor_column in df.columns:
    print(f"Unique values in '{r_factor_column}' column:")
    print(df[r_factor_column].unique())
    
    # Apply satisfaction level calculation
    df['Satisfaction Level'] = df[r_factor_column].apply(get_satisfaction_level)
    
    # Print first few rows to verify
    print("\nFirst few rows after adding Satisfaction Level:")
    print(df[['Timestamp', r_factor_column, 'Satisfaction Level']].head())
else:
    print(f"{r_factor_column} column not found in the dataset.")

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
    plt.figure(figsize=(15, 20))
    
    # Ensure the 'Timestamp' column is sorted for proper plotting
    df = df.sort_values(by='Timestamp')
    
    # Plot 1: Time vs Jitter
    plt.subplot(5, 1, 1)
    plt.plot(df['Timestamp'], df['Jitter (ms)'], marker='o', linestyle='-', color='b')
    plt.xlabel('Time')
    plt.ylabel('Jitter (ms)')
    plt.title('Time vs Jitter')
    plt.grid(True)
    
    # Plot 2: Time vs Packet Loss
    plt.subplot(5, 1, 2)
    plt.plot(df['Timestamp'], df['Packet Loss (%)'], marker='o', linestyle='-', color='r')
    plt.xlabel('Time')
    plt.ylabel('Packet Loss (%)')
    plt.title('Time vs Packet Loss')
    plt.grid(True)
    
    # Plot 3: Time vs Latency
    plt.subplot(5, 1, 3)
    plt.plot(df['Timestamp'], df['Latency (ms)'], marker='o', linestyle='-', color='g')
    plt.xlabel('Time')
    plt.ylabel('Latency (ms)')
    plt.title('Time vs Latency')
    plt.grid(True)
    
    # Plot 4: Distribution of Satisfaction Levels
    if 'Satisfaction Level' in df.columns:
        plt.subplot(5, 1, 4)
        df['Satisfaction Level'].value_counts().plot(kind='bar', color='purple')
        plt.xlabel('Satisfaction Level')
        plt.ylabel('Frequency')
        plt.title('Distribution of Satisfaction Levels')
        plt.grid(True)
    else:
        print("Satisfaction Level column not found in the dataset.")
    
    # Plot 5: Time vs R-Factor
    plt.subplot(5, 1, 5)
    plt.plot(df['Timestamp'], df[r_factor_column], marker='o', linestyle='-', color='orange')
    plt.xlabel('Time')
    plt.ylabel('R-Factor')
    plt.title('Time vs R-Factor')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Plot the metrics
plot_metrics(df)
