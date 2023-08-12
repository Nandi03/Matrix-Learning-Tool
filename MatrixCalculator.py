import numpy as np


class MatrixCalculator:
    def addition(self, matrix1, matrix2):
        return matrix1 + matrix2

    def subtraction(self, matrix1, matrix2):
        return matrix1 - matrix2

    def multiplication(self, matrix1, matrix2):
        return matrix1 * matrix2

    def determinant(self, matrix):
        return np.linalg.det(matrix).astype(int)

    def inverse(self, matrix):
        # det = self.determinant(matrix)
        inverse = (np.linalg.inv(matrix))
        return np.around(inverse, 2)

    def eigenvalues_eigenvectors(self, matrix):
        eig_vals, eig_vects = np.linalg.eig(matrix)
        return np.round(eig_vals, 2), np.round(eig_vects, 2)
