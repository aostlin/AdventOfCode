def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    return arrays


def task1(garden):
    garden_plots = get_garden_plots(garden)
    areas = get_areas(garden_plots)
    total_sum = 0
    for area in areas:
        perimeter = get_perimeter(area, garden_plots)
        total_sum += perimeter * len(area[0])
    return total_sum


def get_garden_plots(garden):
    garden_plots = {}
    for row_idx, row in enumerate(garden):
        for col_idx, col in enumerate(row):
            if col != ".":
                garden_plots.update({(row_idx, col_idx): col})
    return garden_plots


def get_perimeter(area, garden_plots):
    perimeter = 0
    for garden in area[0]:
        neighbors = get_neighbors(garden[0], garden[1])
        neighbors = [x for x in neighbors if (x in garden_plots.keys())]
        neighbors = [x for x in neighbors if garden_plots[x] == area[1]]
        perimeter += 4 - len(neighbors) 
    return perimeter


def get_areas(garden_plots):
    areas = []
    for garden, plant_type in garden_plots.items():
        if garden not in [x for y in areas for x in y[0]]:
            global area
            area = []
            get_area(garden, plant_type, garden_plots)
            areas.append(((list(set(area))), plant_type))
    return areas


def get_area(garden, plant_type, garden_plots):
    area.append(garden)
    neighbors = get_neighbors(garden[0], garden[1])
    neighbors = [x for x in neighbors if (x in garden_plots.keys()) & (x not in area)]
    for neighbor in neighbors:
        if garden_plots[neighbor] == plant_type:
            get_area(neighbor, plant_type, garden_plots)


def get_neighbors(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

if __name__ == "__main__":

    garden = parse_input('./input.dat')

    print(task1(garden))

