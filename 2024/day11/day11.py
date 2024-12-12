
def task1(input_stones):
    total_stones = 0
    for stone in input_stones:
        iteration = 0
        number_of_stones = 0
        number_of_stones = blink(stone, number_of_stones, iteration)
        total_stones += number_of_stones
    return total_stones


def blink(stone, number_of_stones, iteration):
    if iteration == 25:
        number_of_stones += 1
        return number_of_stones
    
    iteration += 1
    if stone == 0:
        number_of_stones = blink(1, number_of_stones, iteration)
    elif len(str(stone)) % 2 == 0:
        stone1, stone2 = split_stone(stone)
        number_of_stones = blink(stone1, number_of_stones, iteration)
        number_of_stones = blink(stone2, number_of_stones, iteration)
    else:
        number_of_stones = blink(stone * 2024, number_of_stones, iteration)
    return number_of_stones


def split_stone(stone):
    stone_to_string = str(stone)
    length = len(stone_to_string)
    return int(stone_to_string[0:int(length/2)]), int(stone_to_string[int(length/2):])


if __name__ == "__main__":

    example_string = '125 17'
    input_string = '112 1110 163902 0 7656027 83039 9 74'

    input_stones = input_string.split()
    input_stones = [int(x) for x in input_stones]

    print(task1(input_stones))

