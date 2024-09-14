# Configuration settings for data stream simulation and anomaly detection
CONFIG = {
    'stream_size': 10000,
    'seasonality': 50,
    'noise_level': 0.5,
    'anomaly_rate': 0.01,
    'drift_start': 3000,           # When concept drift starts
    'drift_rate': 0.1,             # Rate of drift (change in mean)
    'window_size': 100,            # Size of sliding window
    'contamination': 0.01,         # For Isolation Forest
    'use_parallel': True           # Enable parallel processing
}
