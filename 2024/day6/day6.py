def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    return arrays

def task1(field):

    starting_position, obstacles = get_start_and_obstacles(field)

    return len(set(traverse_lab(starting_position, obstacles, field)))-1

def get_start_and_obstacles(field):
    obstacles = []
    for row_idx, row in enumerate(field):
        for col_idx, col in enumerate(row):
            if col == "^":
                starting_position = (row_idx, col_idx)
            if col == "#":
                obstacles.append((row_idx, col_idx))
    return starting_position, obstacles

def traverse_lab(position, obstacles, field):
    new_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}

    visited_spots = [position]
    direction = "^"
    while not (((position[0] < 0) or (position[0] > len(field)-1)) or ((position[1] < 0) or (position[1] > len(field[0])-1))):
        step = next_step(position, direction)
        if step in obstacles:
            direction = new_direction[direction]
        else:
            position = step
            visited_spots.append(position)
            visited_spots = list(set(visited_spots))
    return visited_spots

def traverse_lab_task2(position, obstacles, field):
    new_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}

    direction = "^"
    starting_position = position
    step = position
    path = [(starting_position, direction)]
    while not (((position[0] < 0) or (position[0] > len(field)-1)) or ((position[1] < 0) or (position[1] > len(field[0])-1))):
        step = next_step(position, direction)
        if step in obstacles:
            direction = new_direction[direction]
        else:
            position = step
            new_path = (position, direction)
            if new_path in path:
                return 'Loop detected'
            path.append(new_path)
    return 'Leave lab detected'


def next_step(position, direction):
    i, j = position[0], position[1]
    if direction == ">":
        new_position = (i, j+1)
    elif direction == "<":
        new_position = (i, j-1)
    elif direction == "^":
        new_position = (i-1, j)
    else:
        new_position = (i+1, j)
    return new_position


def task2(field):

    starting_position, obstacles = get_start_and_obstacles(field)
    free_positions = []
    for i in range(len(field)):
        for j in range(len(field[0])):
            free_positions.append((i, j))
    free_positions = [x for x in free_positions if x not in obstacles+[starting_position]]

    count = 0
    for pos, free_position in enumerate(free_positions):
        if pos % 100 == 0:
            print(pos / len(free_positions), count)
        if traverse_lab_task2(starting_position, obstacles+[free_position], field) == 'Loop detected':
            count += 1
    return count


if __name__ == "__main__":

    field = parse_input('./input.dat')

    print(task2(field))
