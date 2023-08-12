from MatrixCalculator import MatrixCalculator
import numpy as np

class Question():
    def __init__(self, size, no_of_matrices, topic):
        self.matrix_size = size
        self.no_of_matrices = no_of_matrices
        self.topic = topic

    def make_matrix(self):
        rand_array = np.random.randint(-15, 15, size=(self.matrix_size, self.matrix_size))
        rand_matrix = np.matrix(rand_array)
        return rand_matrix

    # generates matrices for Q and saves them in txt file
    def make_matrices_for_q(self):
        matrix1 = self.make_matrix()
        calc = MatrixCalculator()
        det = calc.determinant(matrix1)
        while (self.topic == 4 and (det == 0)):
            matrix1 = self.make_matrix()
        self.save_matrices(matrix1)

        if (self.no_of_matrices == 2):
            matrix2 = self.make_matrix()
            self.save_matrices(matrix2)

    def save_matrices(self, matrix):
        f = open('questions.txt', 'a')
        np.savetxt(f, matrix, fmt='%i')
        f.close()