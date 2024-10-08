import unittest
from src.matrix_operations import MatrixOperations

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.A = [[1, 0, 0, -2, -3], [0, 2, 2, 0, 0], [0, 0, 1, 3, 1], [-2, 3, 2, 5, 1]]
        self.matrix_ops = MatrixOperations(self.A)

    def test_replace_row(self):
        result = self.matrix_ops.replace_row(-1, 3, 0)
        expected = [[1, 0, 0, -2, -3], [0, 2, 2, 0, 0], [0, 0, 1, 3, 1], [0, 3, 2, 1, -5]]
        self.assertTrue((result == expected).all())

    def test_switch_rows(self):
        result = self.matrix_ops.switch_rows(0, 1)
        expected = [[0, 2, 2, 0, 0], [1, 0, 0, -2, -3], [0, 0, 1, 3, 1], [-2, 3, 2, 5, 1]]
        self.assertTrue((result == expected).all())

if __name__ == "__main__":
    unittest.main()
