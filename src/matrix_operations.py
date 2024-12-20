import numpy as np

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def replace_row(self, c, i, j):
        E = np.eye(self.matrix.shape[0])
        E[i, :] += c * E[j, :]
        self.matrix = np.dot(E, self.matrix)
        return self.matrix

    def switch_rows(self, i, j):
        E = np.eye(self.matrix.shape[0])
        E[[i, j], :] = E[[j, i], :]
        self.matrix = np.dot(E, self.matrix)
        return self.matrix

    def scale_row(self, c, i):
        E = np.eye(self.matrix.shape[0])
        E[i, :] *= c
        self.matrix = np.dot(E, self.matrix)
        return self.matrix

    def get_matrix(self):
        return self.matrix
