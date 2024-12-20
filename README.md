# Matrix and Vector Operations Library

This project provides a Python library for performing common matrix and vector operations using NumPy. It is designed to aid in understanding linear algebra concepts through row manipulations and vector space operations.

## Project Structure

- `src/matrix_operations.py`: Defines the `MatrixOperations` class for matrix row operations such as row replacement, scaling, and switching.
- `src/vector_operations.py`: Implements the `VectorOperations` class, including methods to check for linear independence and reduce matrices.
- `test_matrix_operations.py`: Contains unit tests for the `MatrixOperations` class to ensure the correctness of its methods.

---

## Features

### Matrix Operations
- **Replace Row:** Replace one row with a combination of itself and another row scaled by a constant.
- **Switch Rows:** Swap two rows within the matrix.
- **Scale Row:** Scale a row by a constant factor.

### Vector Operations
- **Check Linear Independence:** Determines if a set of vectors is linearly independent.
- **Matrix Reduction:** Reduces a matrix using row operations.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jorgebjr28/MatrixOperationsProject.git
