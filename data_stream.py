import numpy as np
import random

def generate_data_stream(pattern_length):
    """
    Generates a sinusoidal data stream with randomized parameters.

    Args:
        pattern_length (int): The length of the data stream (number of data points).

    Returns:
        np.ndarray: An array representing the generated sinusoidal pattern.

    Raises:
        ValueError: If pattern_length is not a positive integer.
    """
    try:
        # Ensure pattern_length is a positive integer
        if not isinstance(pattern_length, int) or pattern_length <= 0:
            raise ValueError("Pattern length must be a positive integer.")

        # Randomly generate the amplitude (A), center value, and phase angle (phi)
        A = random.uniform(20, 100)       # Amplitude: Random value between 20 and 100
        center = random.uniform(50, 150)  # Center value: Random value between 50 and 150
        phi = random.uniform(0, 360)      # Phase angle: Random value between 0 and 360 degrees
        T = 2 * np.pi / 100               # Period: Fixed value for sinusoidal wave

        # Generate the time values for the sinusoidal pattern
        t = np.arange(pattern_length)

        # Create the sinusoidal pattern using the randomized parameters
        sin_pattern = A * np.sin(T * t - np.radians(phi)) + center

        return sin_pattern

    except ValueError as e:
        # Handle invalid pattern_length input
        print(f"Error in generate_data_stream: {e}")


def add_anomalies_to_data(data_stream):
    """
    Adds random anomalies to a given data stream by modifying random positions.

    Args:
        data_stream (list or np.ndarray): The original data stream to which anomalies will be added.

    Raises:
        TypeError: If data_stream is not a list or NumPy array.
    """
    try:
        # Ensure data_stream is either a list or a NumPy array
        if not isinstance(data_stream, (list, np.ndarray)):
            raise TypeError("Data stream must be a list or NumPy array.")

        # Randomize the number of anomalies to be added (between 5 and 10 anomalies)
        num_anomalies = random.randint(5, 10)

        # Randomly select indices to place the anomalies, avoiding the first and last 50 elements
        anomaly_indices = random.sample(range(50, len(data_stream) - 50), num_anomalies)

        for idx in anomaly_indices:
            # Assign a random value to the anomaly (random deviation from normal values)
            data_stream[idx] = random.uniform(10, 70)  # Anomaly value: Random value between 10 and 70

    except TypeError as e:
        # Handle invalid data_stream input
        print(f"Error in add_anomalies_to_data: {e}")
