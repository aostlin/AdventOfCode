import networkx as nx

def parse_input(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            array.append(line.replace('\n', ''))
    return array


def task1(array):

    G = create_graph(array)
    cycles = [c for c in nx.simple_cycles(G, length_bound=3)]
    cycles = [c for c in cycles if (c[0][0] == 't' or c[1][0] == 't' or c[2][0] == 't')]
    return len(cycles)


def task2(array):

    G = create_graph(array)
    return ','.join(sorted(max(nx.find_cliques(G), key=len)))


def create_graph(array):
    G = nx.Graph()
    for line in array:
        G.add_edge(line.split('-')[0], line.split('-')[1])
    return G

    

if __name__ == "__main__":

    array = parse_input('./input.dat')

    print(task2(array))

