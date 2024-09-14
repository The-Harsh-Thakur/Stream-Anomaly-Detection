import random

# Configuration for the anomaly detection and data stream
CONFIG = {
    'pattern_length': 1000,  # Fixed length of the data stream

    # Randomize the number of trees and tree size slightly for each run
    'num_trees': random.randint(30, 50),  # Random number of trees between 30 and 50
    'tree_size': random.randint(200, 300),  # Random tree size between 200 and 300

    # Randomize the size of the sliding window (shingle size)
    'shingle_size': random.randint(3, 6)   # Random window size between 3 and 6
}
