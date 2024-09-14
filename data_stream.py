import numpy as np
from config import CONFIG

def simulate_data_stream():
    size = CONFIG['stream_size']
    seasonality = CONFIG['seasonality']
    noise_level = CONFIG['noise_level']
    anomaly_rate = CONFIG['anomaly_rate']
    drift_start = CONFIG['drift_start']
    drift_rate = CONFIG['drift_rate']

    time = np.arange(size)
    seasonal_pattern = np.sin(2 * np.pi * time / seasonality)
    noise = np.random.normal(0, noise_level, size)
    data = seasonal_pattern + noise

    # Introduce concept drift
    data[drift_start:] += drift_rate * (time[drift_start:] - drift_start)

    # Inject anomalies
    anomalies = np.random.choice([0, 1], size=size, p=[1 - anomaly_rate, anomaly_rate])
    data[anomalies == 1] += np.random.uniform(5, 15, size=np.sum(anomalies))

    return data, anomalies
