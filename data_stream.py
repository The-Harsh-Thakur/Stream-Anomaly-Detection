import numpy as np
import random

def generate_data_stream(pattern_length):
    try:
        if not isinstance(pattern_length, int) or pattern_length <= 0:
            raise ValueError("Pattern length must be a positive integer.")

        # Randomize amplitude, center value, and phase angle
        A = random.uniform(20, 100)       # Random amplitude between 20 and 100
        center = random.uniform(50, 150)  # Random center value between 50 and 150
        phi = random.uniform(0, 360)      # Random phase angle in degrees
        T = 2 * np.pi / 100               # Fixed period (unchanged)
        t = np.arange(pattern_length)
        
        # Generate sinusoidal pattern with random parameters
        sin_pattern = A * np.sin(T * t - np.radians(phi)) + center

        return sin_pattern

    except ValueError as e:
        print(f"Error in generate_data_stream: {e}")

def add_anomalies_to_data(data_stream):
    try:
        if not isinstance(data_stream, (list, np.ndarray)):
            raise TypeError("Data stream must be a list or NumPy array.")

        # Randomize the number and positions of anomalies
        num_anomalies = random.randint(5, 10)  # Random number of anomalies between 5 and 10
        anomaly_indices = random.sample(range(50, len(data_stream)-50), num_anomalies)

        for idx in anomaly_indices:
            # Set a random value for the anomaly (random deviation from the center)
            data_stream[idx] = random.uniform(10, 70)  # Random anomaly value between 10 and 70

    except TypeError as e:
        print(f"Error in add_anomalies_to_data: {e}")
