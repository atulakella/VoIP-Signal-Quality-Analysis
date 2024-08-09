# VoIP Signal Quality Analysis

## Overview

This project focuses on analyzing VoIP (Voice over Internet Protocol) signal quality by examining various network performance metrics. We evaluate how different network conditions impact VoIP signal quality and use these insights to understand the quality of VoIP communications.

## Approach

To tackle the analysis, we generate a synthetic dataset that simulates an original VoIP dataset. This dataset includes the following metrics:

- **Latency (ms)**
- **Jitter (ms)**
- **Packet Loss (%)**

Using this data, we calculate the R-Factor, which is a standard metric for evaluating the quality of a VoIP signal. The R-Factor is computed using the formula:

\[ R\text{-}Factor = 93.2 - Is - Ie - Id \]

Where:
- **Is** = 1.5 × Packet Loss
- **Id** = Jitter × 0.5 (if Jitter is between 30 to 60), Jitter × 1 (if Jitter is above 60)
- **Ie** = (Latency - 150) / 10

We correlate the R-Factor with satisfaction using predefined tables to determine signal quality.

## Metrics and Analysis

The project includes the following analytical components:

1. **Descriptive Statistics**:
   - Mean
   - Maximum
   - Minimum
   - Standard Deviation
   - Other relevant statistics

   These statistics are calculated using SciPy to provide insights into the dataset's characteristics.

2. **Visualization**:
   - A graph displaying metrics vs. time.
   - A graph showing R-Factor vs. time.
   - A frequency distribution of signal quality.

   These visualizations are created using Matplotlib to help illustrate the trends and patterns in the data.

## Results

The results are presented in graphical formats showing how the metrics and R-Factor vary over time and how frequently different levels of signal quality occur. These insights are crucial for assessing VoIP signal performance under various network conditions.

## Contributers
Abhiram Panthangi
