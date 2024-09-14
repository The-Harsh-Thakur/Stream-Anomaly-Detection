from data_stream import simulate_data_stream
from anomaly_detection import detect_anomalies
from visualization import visualize_data

if __name__ == "__main__":
    data, true_anomalies = simulate_data_stream()
    detected_anomalies = detect_anomalies(data)
    visualize_data(data, detected_anomalies)
