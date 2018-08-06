import numpy as np

def imprime_matriz(X):
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            print(X[i,j], end='\t')
        print('\n', end='')
    print('\n')
def soma(X, Y):
    return None

def subtracao(X, Y):
    return None

def multiplicacao_escalar(alpha, X):
    return None

def multiplicacao_matricial(X, Y):
    return None

A = np.array([[2, 6, 7, 9, 12],
              [4, 2, 8, 4, 51],
              [8, 9, 14, 3, 7]])

B = np.array([[2, 6, 7, 9, 12],
              [4, 2, 8, 4, 51],
              [8, 9, 14, 3, 7]])

C = np.array([[1, 0],
              [1, 1],
              [0, 1],
              [0, 0],
              [1, 1]])

imprime_matriz(A)
imprime_matriz(B)
imprime_matriz(C)

R1 = soma(A, B)
R2 = subtracao(A, B)
R3 = multiplicacao_escalar(3, A)
R4 = multiplicacao_matricial(A, C)
