import numpy as np

# all answers will be calculated to 2 decimal places.

# function to generate a matrix with random integer values given the number of rows and columns.
def generate_matrix(rows, columns):
    M = np.random.randint((-15, 15), size=(rows, columns))
    M = str(M)
    M = M.replace("]", " ")
    M = M.replace("[", ";")
    M = M.replace("\n", " ")
    M = M[2:]
    matrix = np.matrix(M)
    return matrix


# function that carries out the matrix addition operation.
def matrix_addition(matrix1, matrix2):
    matrix3 = matrix1 + matrix2
    return matrix3


# function that carries out the matrix subtraction operation.
def matrix_subtraction(matrix1, matrix2):
    matrix3 = matrix1 - matrix2
    return matrix3


# function that carries out the matrix multiplication operation.
def matrix_multiplication(matrix1, matrix2):
    try:
        matrix3 = matrix1 * matrix2
        return matrix3
    # in the case that the number of rows of the first matrix is not equal
    # to the number of columns of the second matrix.
    except:
        print("ERROR. You cannot multiply these matrices together.")


# function that find the determinant of a given matrix.
def matrix_determinant(matrix):
    det = np.linalg.det(matrix)
    det = round(det)
    return det


# function that finds the inverse of a given matrix.
def matrix_inverse(matrix):
    B = np.linalg.inv(matrix)
    inv_a = np.matrix.round(B, 2)
    return inv_a


# function that finds the eigenvalues of a given matrix.
def eigenvalues(matrix):
    B = np.linalg.eigvals(matrix)
    eig_a = np.matrix.round(B, 2)
    return eig_a

