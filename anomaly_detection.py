import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore
from joblib import Parallel, delayed
from config import CONFIG

def detect_anomalies(data):
    # Use sliding windows
    window_size = CONFIG['window_size']
    contamination = CONFIG['contamination']
    use_parallel = CONFIG['use_parallel']
    
    def process_window(window):
        # Combine Isolation Forest with statistical methods like z-score
        iforest = IsolationForest(contamination=contamination)
        window = window.reshape(-1, 1)
        iforest.fit(window)
        predictions = iforest.predict(window)
        z_scores = zscore(window)
        combined_anomalies = (predictions == -1) | (np.abs(z_scores) > 3)
        return combined_anomalies
    
    # Split data into windows
    windows = [data[i:i+window_size] for i in range(0, len(data), window_size)]
    if use_parallel:
        results = Parallel(n_jobs=-1)(delayed(process_window)(window) for window in windows)
    else:
        results = [process_window(window) for window in windows]

    # Flatten results
    anomalies = np.concatenate(results)
    return np.where(anomalies)[0]
