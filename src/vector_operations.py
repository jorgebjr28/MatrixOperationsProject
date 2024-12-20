import numpy as np

class VectorOperations:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def check_linear_independence(self):
        last_row = self.matrix[-1, :]
        return np.any(last_row[:-1])

    def reduce_matrix(self):
        # Perform a sequence of row operations (example logic)
        self.matrix = self.scale_row(0.5, 1)
        self.matrix = self.replace_row(1, 1, 0)
        return self.matrix

    def scale_row(self, c, i):
        E = np.eye(self.matrix.shape[0])
        E[i, :] *= c
        self.matrix = np.dot(E, self.matrix)
        return self.matrix

    def replace_row(self, c, i, j):
        E = np.eye(self.matrix.shape[0])
        E[i, :] += c * E[j, :]
        self.matrix = np.dot(E, self.matrix)
        return self.matrix
