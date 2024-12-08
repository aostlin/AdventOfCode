import numpy as np

def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    return arrays


def create_diagonal_arrays(arrays):
    letter_to_int = {"X": 1, "M": 2, "A": 3, "S": 4}
    int_to_letter = {v: k for k, v in letter_to_int.items()}

    int_array = []
    for array in arrays:
        int_array.append([letter_to_int[x] for x in array])
    int_array = np.array(int_array)

    shape = int_array.shape[0]
    diagonals = []
    for diag in range(-shape+1,shape):
        diagonals.append(np.diagonal(int_array, offset=diag).tolist())

    return [''.join([int_to_letter[x] for x in array]) for array in diagonals]

def task1(arrays):
    vertical_arrays = []
    for idx in range(len(arrays[0])):
        vertical_arrays.append(''.join([x[idx] for x in arrays]))

    diagonal_arrays = create_diagonal_arrays(arrays)
    reversed_arrays = [x[::-1] for x in arrays]
    diagonal_arrays_from_reversed = create_diagonal_arrays(reversed_arrays)

    total_arrays = arrays + vertical_arrays + diagonal_arrays + diagonal_arrays_from_reversed

    count = 0
    for array in total_arrays:
        count += array.count('XMAS')
        count += array.count('SAMX')

    return count

def check_if_xmas(pos, matrix):
    i, j = pos[0], pos[1]
    if matrix[i-1][j+1] == 2 and matrix[i-1][j-1] == 2:
        if matrix[i+1][j+1] == 4 and matrix[i+1][j-1] == 4:
            return True
    elif matrix[i-1][j+1] == 4 and matrix[i-1][j-1] == 4:
        if matrix[i+1][j+1] == 2 and matrix[i+1][j-1] == 2:
            return True
    elif matrix[i-1][j+1] == 2 and matrix[i+1][j+1] == 2:
        if matrix[i-1][j-1] == 4 and matrix[i+1][j-1] == 4:
            return True
    elif matrix[i-1][j+1] == 4 and matrix[i+1][j+1] == 4:
        if matrix[i-1][j-1] == 2 and matrix[i+1][j-1] == 2:
            return True
    return False

def task2(arrays):
    letter_to_int = {"X": 1, "M": 2, "A": 3, "S": 4}

    int_array = []
    for array in arrays:
        int_array.append([letter_to_int[x] for x in array])
    int_array = np.array(int_array)
    shape = int_array.shape[0]

    all_a_indices = np.where(int_array == 3)
    all_a_not_on_border = [(i,j) for i, j in zip(all_a_indices[0], all_a_indices[1]) if i not in [0,shape-1] and j not in [0,shape-1]]

    count = 0
    for pos in all_a_not_on_border:
        if check_if_xmas(pos, int_array):
            count += 1

    return count


if __name__ == "__main__":

    arrays = parse_input('./input.dat')

    print(task2(arrays))

    