import math

def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    program = []
    register_a = 0
    register_b = 0
    register_c = 0
    for line in arrays:
        if line.split(':')[0] == "Program":
            program = line.split(':')[1].split(',')
        if line.split(':')[0] == "Register A":
            register_a = int(line.split(':')[1])
        if line.split(':')[0] == "Register B":
            register_b = int(line.split(':')[1])
        if line.split(':')[0] == "Register C":
            register_c = int(line.split(':')[1])
    program = [int(x) for x in program]
    return register_a, register_b, register_c, program


def task1(register_a, register_b, register_c, program):

    register = {"A": register_a, "B": register_b, "C": register_c}

    output = []

    i = 0
    while i < len(program):

        operand_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: register["A"], 5: register["B"], 6: register["C"]}
        opcode = program[i]
        operand = program[i+1]

        if opcode == 0:
            adv = register["A"] / 2**operand_dict[operand]
            register["A"] = math.floor(adv)
            i += 2

        if opcode == 1:
            register["B"] = register["B"] ^ operand
            i += 2

        if opcode == 2:
            register["B"] = operand_dict[operand] % 8
            i += 2

        if opcode == 3:
            if register["A"] != 0:
                i = operand
            else:
                i += 2

        if opcode == 4:
            register["B"] = register["B"] ^ register["C"]
            i += 2

        if opcode == 5:
            output.append(operand_dict[operand] % 8)
            i += 2

        if opcode == 6:
            adv = register["A"] / 2**operand_dict[operand]
            register["B"] = math.floor(adv)
            i += 2

        if opcode == 7:
            adv = register["A"] / 2**operand_dict[operand]
            register["C"] = math.floor(adv)
            i += 2

    return output, register

if __name__ == "__main__":

    register_a, register_b, register_c, program = parse_input('./input.dat')

    print(task1(register_a, register_b, register_c, program)[0])