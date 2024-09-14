# Import necessary modules and functions from other project files
from data_stream import generate_data_stream, add_anomalies_to_data
from rct_forest import RCTreeForest
from visualization import visualize_data
from config import CONFIG

def run_anomaly_detection():
    """
    Main function that generates a data stream, detects anomalies using RCTreeForest,
    and visualizes both the data stream and the detected anomalies.
    """
    # Step 1: Generate a data stream with random parameters from the config file
    data_stream = generate_data_stream(CONFIG['pattern_length'])

    # Step 2: Introduce anomalies to the generated data stream
    add_anomalies_to_data(data_stream)

    # Step 3: Initialize the RCTreeForest for anomaly detection using random parameters from the config file
    forest = RCTreeForest(CONFIG['num_trees'], CONFIG['tree_size'], CONFIG['shingle_size'])

    # Step 4: Initialize lists to hold anomaly scores and the sliding window of data points
    anomaly_scores = []  # Stores the calculated anomaly scores for each data point
    current_window = []  # A sliding window that holds the last `shingle_size` data points

    # Step 5: Iterate over the data stream and detect anomalies
    for i in range(len(data_stream)):
        # If still filling the window (i.e., index is smaller than shingle size)
        if i < forest.shingle_size:
            current_window.append(data_stream[i])  # Add data point to the window
            anomaly_scores.append(0)  # Set anomaly score to 0 for the initial points
        else:
            # Slide the window: add new data point and remove the oldest one
            current_window.append(data_stream[i])
            current_window = current_window[1:]

            # Calculate the anomaly score for the current window using RCTreeForest
            score = forest.anomaly_detector(i, current_window)
            anomaly_scores.append(score)  # Append the anomaly score to the list

            # Step 6: Detect sudden peaks in anomaly score to flag an anomaly
            if i > forest.shingle_size and abs(score - anomaly_scores[i-1]) > 1.7 * anomaly_scores[i-1]:
                print(f"Anomaly detected at index: {i}")  # Log the detected anomaly with its index

    # Step 7: Visualize the original data stream and the calculated anomaly scores
    visualize_data(data_stream, anomaly_scores)

# Entry point of the script
if __name__ == "__main__":
    run_anomaly_detection()  # Call the main function to run the anomaly detection process
