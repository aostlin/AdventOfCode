
def task1(input_string):
    return compute_checksum(create_filled_list(input_string))


def compute_checksum(output_list):
    return sum([idx * x for idx, x in enumerate(output_list)]) 


def create_filled_list(input_string):

    nr_filled = sum([int(x) for x in input_string[::2]])

    reverse_list_gen = explode_list_reverse(input_string)
    list_gen = explode_list(input_string)

    exploded_list = [] 
    for idx, x in enumerate(input_string):
        if idx % 2 == 0:
            for x in range(int(x)):
                exploded_list.append(next(list_gen))
        else:
            for x in range(int(x)):
                exploded_list.append(next(reverse_list_gen))
        if len(exploded_list) >= nr_filled:
            break

    remainder = len(exploded_list) - nr_filled
    if len(exploded_list) > nr_filled:
        return exploded_list[:len(exploded_list)-remainder]
    else:
        return exploded_list  


def reverse_enumerate(input_list):
    for idx in range(len(input_list)-1, -1, -1):
        yield (idx, input_list[idx])


def explode_list_reverse(input_string):
   for idx, x in reverse_enumerate(input_string[::2]):
      for _ in range(int(x)):
        yield idx


def explode_list(input_string):
   for idx, x in enumerate(input_string[::2]):
      for _ in range(int(x)):
        yield idx


if __name__ == "__main__":

    example_string = "2333133121414131402" # "12345"

    with open('./input.dat', 'r') as file:
        input_string = file.read()

    print(task1(input_string))
