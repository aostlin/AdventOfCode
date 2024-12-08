from collections import defaultdict

def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    return arrays


def get_antenna_positions(field):
    antenna_positions = defaultdict(list)
    for row_idx, row in enumerate(field):
        for col_idx, col in enumerate(row):
            if col != ".":
                antenna_positions[col].append((row_idx, col_idx))
    return antenna_positions

def compute_antinodes(antenna1, antenna2):
    dx, dy = compute_distance(antenna1, antenna2)
    antinode1 = (antenna1[0]+dy, antenna1[1]+dx)
    antinode2 = (antenna2[0]-dy, antenna2[1]-dx)
    return antinode1, antinode2


def compute_distance(antenna1, antenna2):
    dy = antenna1[0] - antenna2[0]
    dx = antenna1[1] - antenna2[1]
    return dx, dy

def task1(field):
     
    antenna_positions = get_antenna_positions(field)

    antinodes = []
    for antenna_type in antenna_positions:
        antennas = antenna_positions[antenna_type]
        for _ in range(len(antennas)):
            antenna1 = antennas.pop(0)
            for antenna2 in antennas:
                antinode1, antinode2 = compute_antinodes(antenna1, antenna2)
                antinodes.append(antinode1)
                antinodes.append(antinode2)

    xlimit = len(field[0])-1
    ylimit = len(field)-1
    antinodes = [x for x in antinodes if ((0 <= x[1] <= xlimit) and (0 <= x[0] <= ylimit))]
    return list(set(antinodes))


def task2(field):
     
    antenna_positions = get_antenna_positions(field)

    xlimit = len(field[0])-1
    ylimit = len(field)-1

    antinodes = []
    for antenna_type in antenna_positions:
        antennas = antenna_positions[antenna_type]
        for _ in range(len(antennas)):
            antenna1 = antennas.pop(0)
            for antenna2 in antennas:
                dx, dy = compute_distance(antenna1, antenna2)
                antinode1 = (antenna1[0]-dy, antenna1[1]-dx)
                antinode2 = (antenna2[0]+dy, antenna2[1]+dx)
                if within_boundary(antinode1, xlimit, ylimit):
                    antinodes.append(antinode1)
                if within_boundary(antinode2, xlimit, ylimit):
                    antinodes.append(antinode2)    
                while within_boundary(antinode1, xlimit, ylimit):
                    antinode1 = (antinode1[0]-dy, antinode1[1]-dx)
                    antinodes.append(antinode1)
                while within_boundary(antinode2, xlimit, ylimit):
                    antinode2 = (antinode2[0]+dy, antinode2[1]+dx)
                    antinodes.append(antinode2)

    antinodes = [x for x in antinodes if ((0 <= x[1] <= xlimit) and (0 <= x[0] <= ylimit))]
    return list(set(antinodes))


def within_boundary(antinode, xlimit, ylimit):
    if ((0 <= antinode[1] <= xlimit) and (0 <= antinode[0] <= ylimit)):
        return True
    return False


if __name__ == "__main__":

    field = parse_input('./input.dat')

    print(len(task2(field)))