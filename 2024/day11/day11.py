def task(input_stones):
    total_stones = 0
    global memo
    memo = {}
    for stone in input_stones:
        iteration = 0
        total_stones += blink(stone, iteration)
    return total_stones


def blink(stone, iteration):
    iteration += 1
    if (stone, iteration) in memo:
        return memo[(stone, iteration)]
    if iteration == 76:
        return 1
    
    if stone == 0:
        memo.update({(stone, iteration) : blink(1, iteration)})
    elif len(str(stone)) % 2 == 0:
        stone1, stone2 = split_stone(stone)
        memo.update({(stone, iteration) : blink(stone1, iteration) + blink(stone2, iteration)})
    else:
        memo.update({(stone, iteration) : blink(stone * 2024, iteration)})
    return memo[(stone, iteration)]


def split_stone(stone):
    stone_to_string = str(stone)
    length = len(stone_to_string)
    return int(stone_to_string[0:int(length/2)]), int(stone_to_string[int(length/2):])


if __name__ == "__main__":

    example_string = '125 17'
    input_string = '112 1110 163902 0 7656027 83039 9 74'

    input_stones = input_string.split()
    input_stones = [int(x) for x in input_stones]

    print(task(input_stones))

