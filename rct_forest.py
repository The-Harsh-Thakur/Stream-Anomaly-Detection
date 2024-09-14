import rrcf
from config import CONFIG

class RCTreeForest:
    def __init__(self, num_ttrees, tree_size, window_size):
        """
        Initialize the Random Cut Tree (RCT) Forest.

        Args:
            num_trees (int): Number of trees in the forest.
            tree_size (int): Maximum number of points that each tree can store.
            window_size (int): Size of the sliding window (shingle size) for the data.

        Raises:
            ValueError: If any of the input parameters are not positive integers.
        """
        try:
            # Ensure that all input parameters are positive integers
            if not all(isinstance(param, int) and param > 0 for param in [num_ttrees, tree_size, window_size]):
                raise ValueError("All parameters must be positive integers.")

            # Store the number of trees, tree size, and shingle size
            self.num_trees = num_ttrees
            self.tree_size = tree_size
            self.shingle_size = window_size

            # Create a forest with the specified number of RCTrees
            self.forest = [rrcf.RCTree() for _ in range(num_ttrees)]

        except ValueError as e:
            # Handle value error if parameters are invalid
            print(f"Error in initialization: {e}")

    def anomaly_detector(self, index, point):
        """
        Detect anomalies by calculating the average codisplacement for a point.

        Args:
            index (int): Index of the current point in the data stream.
            point (list): A list of numeric values representing a data point in the sliding window (shingle).

        Returns:
            float: The average codisplacement score for the given point, used as the anomaly score.

        Raises:
            ValueError: If index is negative, or if point is not a list of numeric values with the correct length.
        """
        try:
            # Ensure the index is a non-negative integer
            if not isinstance(index, int) or index < 0:
                raise ValueError("Index must be a non-negative integer.")

            # Ensure the point is a list of numeric values and matches the shingle size
            if not isinstance(point, list) or len(point) != self.shingle_size or not all(isinstance(p, (int, float)) for p in point):
                raise ValueError(f"Point must be a list of {self.shingle_size} numeric values.")

            # Initialize the average codisplacement for the current point
            avg_codisplacement = 0

            # Iterate over each tree in the forest
            for tree in self.forest:
                # If the tree has exceeded its size limit, forget the oldest point
                if len(tree.leaves) > self.tree_size:
                    tree.forget_point(index - self.tree_size)

                # Insert the current point into the tree
                tree.insert_point(point, index=index)

                # Compute the codisplacement for the current point and add it to the average
                avg_codisplacement += tree.codisp(index) / self.num_trees

            # Return the average codisplacement score (anomaly score)
            return avg_codisplacement

        except ValueError as e:
            # Handle value error if parameters are invalid
            print(f"Error in anomaly detection: {e}")
