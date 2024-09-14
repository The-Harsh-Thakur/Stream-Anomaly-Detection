import rrcf
from config import CONFIG

class RCTreeForest:
    def __init__(self, num_trees, tree_size, window_size):
        try:
            if not all(isinstance(param, int) and param > 0 for param in [num_trees, tree_size, window_size]):
                raise ValueError("All parameters must be positive integers.")

            self.num_trees = num_trees
            self.tree_size = tree_size
            self.shingle_size = window_size
            self.forest = [rrcf.RCTree() for _ in range(num_trees)]

        except ValueError as e:
            print(f"Error in initialization: {e}")

    def anomaly_detector(self, index, point):
        try:
            if not isinstance(index, int) or index < 0:
                raise ValueError("Index must be a non-negative integer.")
            if not isinstance(point, list) or len(point) != self.shingle_size or not all(isinstance(p, (int, float)) for p in point):
                raise ValueError(f"Point must be a list of {self.shingle_size} numeric values.")

            avg_codisplacement = 0
            for tree in self.forest:
                if len(tree.leaves) > self.tree_size:
                    tree.forget_point(index - self.tree_size)

                tree.insert_point(point, index=index)
                avg_codisplacement += tree.codisp(index) / self.num_trees

            return avg_codisplacement

        except ValueError as e:
            print(f"Error in anomaly detection: {e}")
