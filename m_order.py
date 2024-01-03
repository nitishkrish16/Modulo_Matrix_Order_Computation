
import itertools


def generate_matrices(arr, p):
    matrices = {}
    for a, b, c, d in itertools.product(arr, repeat=4):
        det = (a*d - b*c) % p
        if det == 1:
            matrix = [[a, b], [c, d]]
            # get the dimensions of the matrix
            rows, cols = len(matrix), len(matrix[0])
            # calculate the powers of the matrix until it equals the identity matrix
            n = 1
            identity = [[1, 0], [0, 1]]
            while not matrix_equals(matrix_power(matrix, n, p), identity):
                n += 1
            matrices[str(matrix)] = n
    return matrices

def matrix_multiply(A, B, p):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A == rows_B
    C = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= p
    return C

def matrix_power(A, n, p):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return A
    else:
        half = matrix_power(A, n // 2, p)
        if n % 2 == 0:
            return matrix_multiply(half, half, p)
        else:
            return matrix_multiply(matrix_multiply(half, half, p), A, p)

def matrix_equals(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if rows_A != rows_B or cols_A != cols_B:
        return False
    for i in range(rows_A):
        for j in range(cols_A):
            if A[i][j] != B[i][j]:
                return False
    return True

p=23
arr = [x for x in range(p)]

m = generate_matrices(arr,p)
matrix_list = list(m.keys())
print(m)
print("\n\n")

count_dict = {}
numbers = list(m.values())
for i in range(1,max(numbers)+1):
    count_dict[i] = numbers.count(i)

print("Order        no of elements")
print("\n")
for key,value in count_dict.items():
    print(key,"           ",value)
    print("\n")
    
