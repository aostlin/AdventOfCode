def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    return arrays


def task(hike_map, task):
    parsed_map = parse_map(hike_map)
    x_max = len(hike_map[0]) - 1
    y_max = len(hike_map) - 1
    trail_starts = find_trail_starts(parsed_map)
    endpoint_score = find_endpoints(trail_starts, parsed_map, x_max, y_max, task)
    return endpoint_score


def parse_map(hike_map):
    parsed_map = {}
    for idy, row in enumerate(hike_map):
        for idx, height in enumerate(row):
            parsed_map[(idx, idy)] = int(height)
    return parsed_map


def find_trail_starts(parsed_map):
    return [k for k, v in parsed_map.items() if v == 0]


def find_endpoints(trail_starts, parsed_map, x_max, y_max, task):
    total_score = 0
    for trail_start in sorted(trail_starts):
        endpoints = []
        endpoints = find_next_step(trail_start, parsed_map, endpoints, x_max, y_max)
        if task == 1:
            total_score += len(set(endpoints))
        elif task == 2:
            total_score += len(endpoints)
        else:
            print('Task should be 1 or 2')
    return total_score


def find_next_step(position, parsed_map, endpoints, x_max, y_max):
    neigbors = get_valid_neigbors(position, parsed_map, x_max, y_max)
    for neigbor in neigbors:
        if parsed_map[neigbor] == 9:
            endpoints.append(neigbor)
        else:
            endpoints = find_next_step(neigbor, parsed_map, endpoints, x_max, y_max)
    return endpoints


def get_valid_neigbors(position, parsed_map, x_max, y_max):
    x, y = position[0], position[1]
    neigbors = []
    current_val = parsed_map[position]
    if 0 <= x+1 <= x_max:
        if parsed_map[(x+1,y)] == current_val + 1:
            neigbors.append((x+1, y))
    if 0 <= x-1 <= x_max:
        if parsed_map[(x-1,y)] == current_val + 1:
            neigbors.append((x-1, y))
    if 0 <= y+1 <= y_max:
        if parsed_map[(x,y+1)] == current_val + 1:
            neigbors.append((x, y+1))
    if 0 <= y-1 <= y_max:
        if parsed_map[(x,y-1)] == current_val + 1:
            neigbors.append((x, y-1))
    return neigbors


if __name__ == "__main__":

    hike_map = parse_input('./input.dat')

    print(task(hike_map, task=2))

