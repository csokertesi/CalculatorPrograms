def input_matrix(size):
    matrix = [[int(input(f"{x},{y}: ")) for x in range(size)] for y in range(size)]
    return matrix

def det(matrix):
    if len(matrix) == 0 or len(matrix[0]) != len(matrix):
        raise ValueError("Non-square matrix!")

    size = len(matrix)

    # 2x2 matrix determinant
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0

    # Loop first row
    # i: index (column)
    # coeff: value
    for i, coeff in enumerate(matrix[0]):
        # Negate every second coefficient
        coeff *= 1 if i % 2 == 0 else -1

        # Construct sub-matrix without first row and current column
        sub_matrix = [
                [x for x in matrix[r][0:i]+matrix[r][i+1:size]] for r in range(1, size)
            ]
        
        # Add product of coefficient and the determinant of the sub-matrix to the sum
        determinant += coeff * det(sub_matrix)
    
    return determinant


print(det(input_matrix(input("Size: ")))
