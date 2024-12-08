def parse_input(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            array.append(list(map(int, line.split())))

    return array

def create_diff_array(array):
    return [x - y for x, y in zip(array[:-1],array[1:])]

def is_valid(array):
    if len(array) == 1:
        return False
    diff_array = create_diff_array(array)
    neg_sign = [x < 0  for x in diff_array]
    pos_sign = [x > 0  for x in diff_array]
    correct_diff = [abs(x) < 4  for x in diff_array]
    return (all(neg_sign) | all(pos_sign)) & all(correct_diff)

def task1(arrays):
    return sum([1 if is_valid(array) else 0 for array in arrays])

def task2(arrays):
    i = 0
    for array in arrays:
        if is_valid(array):
            i += 1
        else:
            for idx, value in enumerate(array):
                if is_valid([x for index, x in enumerate(array) if index != idx]):
                    print([x for x in array if x != value])
                    i += 1
                    break
    return i



if __name__ == "__main__":

    arrays = parse_input('./input.dat')

    #print(task1(arrays))

    print(task2(arrays))