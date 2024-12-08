from collections import defaultdict


def parse_input(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            arrays.append(line.replace('\n', ''))
    rule_array, update_array = [], []
    for array in arrays:
        if "|" in array:
            rule_array.append(array)
        if "," in array:
            update_array.append(array)
    return rule_array, update_array


def task1(rule_array, update_array):

    rule_dict = create_rule_dict(rule_array)
    count = 0
    for update in update_array:
        update = update.split(',')
        middle = int(update[int((len(update)-1)/2)])
        if is_valid(update, rule_dict):
            count += middle
    return count


def create_rule_dict(rule_array):
    rule_dict = defaultdict(list)
    for rule in rule_array:
        key, item = rule.split("|")[0], rule.split("|")[1]
        rule_dict[key].append(item)
    return rule_dict


def is_valid(update, rule_dict):
    for _ in range(len(update)):
            key = update.pop(0)
            if len(set(update) - set(rule_dict[key])) != 0:
                return False
    return True


def task2(rule_array, update_array):

    rule_dict = create_rule_dict(rule_array)
    count = 0
    for update in update_array:
        update = update.split(',')
        update_copy = update.copy()
        if not is_valid(update.copy(), rule_dict):
            while not is_valid(update_copy.copy(), rule_dict):
                for idx in range(len(update_copy)-1):
                    if update_copy[idx+1] not in rule_dict[update_copy[idx]]:
                        update_copy[idx+1], update_copy[idx] = update_copy[idx], update_copy[idx+1]
                middle = int(list(update_copy)[int((len(update_copy)-1)/2)])
            count += middle
    return count


if __name__ == "__main__":

    rule_array, update_array = parse_input('./input.dat')
    
    print(task2(rule_array, update_array))