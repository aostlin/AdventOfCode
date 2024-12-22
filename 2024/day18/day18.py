import networkx as nx

def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    bytes = []
    for line in arrays:
        bytes.append((int(line.split(',')[0]), int(line.split(',')[1])))
    return bytes


def task1(bytes):

    size = 70
    cutoff = 1024

    bytes_until_cutoff = bytes[:cutoff]

    free_space = []
    for x in range(size+1):
        for y in range(size+1):
            if (x, y) not in bytes_until_cutoff:
                free_space.append((x, y))

    G = create_graph(free_space)

    return nx.shortest_path_length(G, source=(0,0), target=(size, size))


def task2(bytes):

    size = 70
    cutoff = 1024

    bytes_until_cutoff = bytes[:cutoff]

    free_space = []
    for x in range(size+1):
        for y in range(size+1):
            if (x, y) not in bytes_until_cutoff:
                free_space.append((x, y))

    G = create_graph(free_space)

    while nx.has_path(G, source=(0,0), target=(size, size)):
        cutoff += 1
        bytes_until_cutoff = bytes[:cutoff]
        G.remove_node(bytes_until_cutoff[-1])

    return bytes_until_cutoff[-1]


def create_graph(free_space):
    G = nx.Graph()

    G.add_nodes_from(free_space)
    for node in free_space:
        neighbors = get_neighbors(node[0], node[1])
        for neighbor in neighbors:
            if neighbor in free_space:
                G.add_edge(node, neighbor)

    return G


def get_neighbors(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


if __name__ == "__main__":

    bytes = parse_input('./input.dat')

    print(task2(bytes))