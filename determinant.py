def input_matrix():
    size = int(input("Size: "))
    matrix = [[int(input(f"{x}, {y}: ")) for x in range(size)] for y in range(size)]
    return matrix

def print_matrix(matrix):
    size = len(matrix)
    print("-" * 2 * size)
    for row in range(size):
        print(''.join([f"{x} " for x in matrix[row]]))
    print("-" * 2 * size)
    

def det(matrix):
    if len(matrix) == 0 or len(matrix[0]) != len(matrix):
        raise ValueError("Non-square matrix!")

    size = len(matrix)
    
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for i, coeff in enumerate(matrix[0]):
        coeff *= 1 if i % 2 == 0 else -1
        subMatrix = [
                [x for x in matrix[r][0:i]+matrix[r][i+1:size]] for r in range(1, size)
            ]
        determinant += coeff * det(subMatrix)
    return determinant
        
print(det(input_matrix()))
