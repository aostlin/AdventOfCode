import numpy as np
import matplotlib.pyplot as plt

def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    positions = []
    velocities = []
    for line in arrays:
        positions.append((int(line.split()[0].split("=")[1].split(",")[0]), int(line.split()[0].split("=")[1].split(",")[1])))
        velocities.append((int(line.split()[1].split("=")[1].split(",")[0]), int(line.split()[1].split("=")[1].split(",")[1])))
    return positions, velocities


def task1(positions, velocities):
    number_of_seconds = 100
    width = 101
    height = 103
    new_positions = get_new_positions(positions, velocities, number_of_seconds, width, height)
    first_quadrant, second_quadrant, third_quadrant, fourth_quadrant = get_safety_factor(new_positions, width, height)
    return first_quadrant * second_quadrant * third_quadrant * fourth_quadrant


def get_new_positions(positions, velocities, number_of_seconds, width, height):
    new_positions = []
    for position in [(p[0]+number_of_seconds*v[0], p[1]+number_of_seconds*v[1])for p, v in zip(positions, velocities)]:
        new_positions.append((position[0] % width, position[1] % height))
    return new_positions


def get_safety_factor(positions, width, height):
    first_quadrant, second_quadrant, third_quadrant, fourth_quadrant = 0, 0, 0, 0
    for position in positions:
        if ((width-1) / 2 < position[0]) & (position[1] < (height-1) / 2):
            first_quadrant += 1
        if (position[0] < (width-1) / 2) & (position[1] < (height-1) / 2):
            second_quadrant += 1 
        if (position[0] < (width-1) / 2) & (position[1] > (height-1) / 2):
            third_quadrant += 1
        if (position[0] > (width-1) / 2) & (position[1] > (height-1) / 2):
            fourth_quadrant += 1
    return first_quadrant, second_quadrant, third_quadrant, fourth_quadrant


def task2(positions, velocities):
    width = 101
    height = 103
    for number_of_seconds in range(1,10402): # "magic number" found by iterating until the starting positions returned
        new_positions = get_new_positions(positions, velocities, 1, width, height)
        first_quadrant, second_quadrant, third_quadrant, fourth_quadrant = get_safety_factor(new_positions, width, height)
        if any([first_quadrant < 50, second_quadrant < 50, third_quadrant < 50, fourth_quadrant < 50]):
            matrix = create_matrix_for_plotting(new_positions, width, height)
            plt.imshow(matrix)
            plt.savefig(f"./xmas_tree_{number_of_seconds}.png")
        positions = new_positions


def create_matrix_for_plotting(positions, width, height):
    matrix = np.zeros((height, width))

    for position in positions:
        matrix[position[1]][position[0]] = 1

    return matrix


if __name__ == "__main__":

    positions, velocities = parse_input('./input.dat')
    task2(positions, velocities)