#from collections import defaultdict

def parse_input(warehouse_path, directions_path):
    arrays = []
    with open(warehouse_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))

    warehouse = {}
    for row_idx, row in enumerate(arrays):
        for col_idx, col in enumerate(row):
            warehouse.update({(col_idx, row_idx) : col})

    arrays = []
    with open(directions_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    directions = ""
    for array in arrays:
        directions += array

    return warehouse, directions 
    

def task1(warehouse, directions):

    for direction in directions:
        current_position = [k for k, v in warehouse.items() if v == "@"][0]
        x, y = intended_step(current_position[0], current_position[1], direction)
        if warehouse[(x,y)] == "#":
            continue
        elif warehouse[(x,y)] == ".":
            warehouse.update({(current_position[0], current_position[1]) : "."})
            warehouse.update({(x, y) : "@"})
        else:
            assert warehouse[(x,y)] == "O"
            new_positions=[]
            movable, new_obstacle_positions = obstacle_movable((x,y), direction, warehouse, new_positions)
            if movable:
                warehouse.update({(current_position[0], current_position[1]) : "."})
                for position in new_obstacle_positions:
                    warehouse.update({position : "O"})
                warehouse.update({(x, y) : "@"})

    return sum([100*k[1] + k[0] for k, v in warehouse.items() if v == "O"])


def obstacle_movable(position, direction, warehouse, new_positions):
    x, y = intended_step(position[0], position[1], direction)
    if warehouse[(x, y)] == "#":
        return False, new_positions
    if warehouse[(x, y)] == ".":
        new_positions.append((x,y))
        return True, new_positions
    else:
        new_positions.append((x,y))
        return obstacle_movable((x,y), direction, warehouse, new_positions)


def intended_step(x, y, direction):
    if direction == "^":
        return x, y-1
    elif direction == "v":
        return x, y+1
    elif direction == ">":
        return x+1, y
    else:
        return x-1, y


if __name__ == "__main__":

    warehouse, directions = parse_input('./warehouse.dat', 'directions.dat')

    print(warehouse)

    print(task1(warehouse, directions))
    