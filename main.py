from data_stream import generate_data_stream, add_anomalies_to_data
from rct_forest import RCTreeForest
from visualization import visualize_data
from config import CONFIG

def run_anomaly_detection():
    # Generate and modify data stream with random parameters
    data_stream = generate_data_stream(CONFIG['pattern_length'])
    add_anomalies_to_data(data_stream)

    # Initialize RCTreeForest with randomized parameters
    forest = RCTreeForest(CONFIG['num_trees'], CONFIG['tree_size'], CONFIG['shingle_size'])

    # Initialize lists for anomaly scores and the sliding window
    anomaly_scores = []
    current_window = []

    # Process the data stream
    for i in range(len(data_stream)):
        if i < forest.shingle_size:
            current_window.append(data_stream[i])
            anomaly_scores.append(0)
        else:
            current_window.append(data_stream[i])
            current_window = current_window[1:]

            # Calculate anomaly score
            score = forest.anomaly_detector(i, current_window)
            anomaly_scores.append(score)

            # Anomaly detection based on score deviation
            if i > forest.shingle_size and abs(score - anomaly_scores[i-1]) > 1.7 * anomaly_scores[i-1]:
                print(f"Anomaly detected at index: {i}")

    # Visualize the data stream and anomaly scores
    visualize_data(data_stream, anomaly_scores)

if __name__ == "__main__":
    run_anomaly_detection()
