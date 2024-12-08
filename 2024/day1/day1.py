from collections import Counter

def parse_input(file_path):
    array1 = []
    array2 = []
    with open(file_path, 'r') as file:
        for line in file:
            array1.append(int(line.split()[0]))
            array2.append(int(line.split()[1]))

    return array1, array2

def task1(array1, array2):

    return sum([abs(x-y) for x, y in zip(sorted(array1), sorted(array2))])

def task2(array1, array2):

    multiplicity = Counter(array2)

    return sum([multiplicity[x] * x for x in array1])

if __name__ == "__main__":

    array1, array2 = parse_input('./input.dat')

    # print(task1(array1, array2))

    print(task2(array1, array2))

