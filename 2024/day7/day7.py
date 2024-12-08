import operator
from itertools import product

def parse_input(file_path):
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            equations.append(line.replace('\n', ''))
    return equations


def task1(equations):
    total_result = 0
    for equation in equations:
        total_result += valid_equation(equation)
    return total_result


def valid_equation(equation, include_concat=False):
    expected_result, inputs = int(equation.split(':')[0]), equation.split(':')[1].split()
    inputs = [int(x) for x in inputs]
    operator_seqs = [x for x in product([operator.mul, operator.add, operator.concat], repeat=(len(inputs)-1))] if include_concat else [x for x in product([operator.mul, operator.add], repeat=(len(inputs)-1))]
    for op_seq in operator_seqs:
        if compute_equation(inputs, op_seq) == expected_result:
            return expected_result
    return 0


def compute_equation(inputs, op_seq):
    cum_res = inputs[0]
    for i in range(len(inputs)-1):
        if op_seq[i] != operator.concat:
            cum_res = op_seq[i](cum_res, inputs[i+1])
        else:
            cum_res = int(op_seq[i](str(cum_res), str(inputs[i+1])))
    return cum_res


def task2(equations):
    total_result = 0
    for equation in equations:
        total_result += valid_equation(equation, include_concat=True)
    return total_result


if __name__ == "__main__":

    equations = parse_input('./input.dat')

    print(task2(equations))
