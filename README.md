# Efficient Data Stream Anomaly Detection

## Project Description
This project implements a Python-based solution for detecting anomalies in a continuous data stream. The data stream, which simulates real-time sequences of floating-point numbers, could represent various metrics like financial transactions or system metrics. The primary focus is on identifying unusual patterns, such as exceptionally high values or deviations from normal behavior.

## How It Works

1. **Data Stream Generation**:
   - A sinusoidal data stream is generated using randomized parameters such as amplitude, phase angle, and center value to simulate seasonal variations.
   - Anomalies are introduced by randomly altering certain values in the stream.

2. **Anomaly Detection**:
   - The project uses the Random Cut Tree (RCT) algorithm to detect anomalies. This algorithm analyzes patterns in the data and calculates anomaly scores based on deviations from expected values.
   - Anomalies are flagged when there is a sudden and significant change in the anomaly score compared to the previous data points.

3. **Real-Time Visualization**:
   - The data stream and corresponding anomaly scores are visualized in real-time using Plotly. The plot includes two lines: one for the data stream and another for the anomaly scores.
   - Anomalies are highlighted on the plot, making it easy to identify points of interest.

## Running the Project

1. **Clone the repository or download the project files.**

2. **Install the necessary dependencies using:**
   ```bash
   pip install -r requirements.txt

3. **Run the project by executing the main.py script.**

## Explanation of the Algorithm
Random Cut Tree (RCT): The RCT algorithm builds a forest of trees where each tree is constructed by making random cuts in the data space. As new data points are streamed, they are inserted into the trees, and anomaly scores are calculated based on the structural changes they introduce. If a point significantly disrupts the structure, it is likely an anomaly.
The RCT approach is efficient for detecting both global and local anomalies in real-time data streams, and it adapts to changes in the data patterns (concept drift).
