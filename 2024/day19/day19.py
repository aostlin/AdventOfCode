def parse_input(pattern_path, layout_path):
    layouts = []
    with open(pattern_path, 'r') as file:
        content = file.read()
    patterns = content.split(', ')
    with open(layout_path, 'r') as file:
        for line in file:
            layouts.append(line.replace('\n', ''))
    return patterns, layouts


def task1(patterns, layouts):
    count = 0
    for layout in layouts:
        if len(check_layout(patterns, layout)) == len(layout):
            count += 1
    return count


def check_layout(patterns, layout):
    total_strings = []
    for pattern in patterns:
        if pattern in layout:
            total_strings.extend([x for y in [x for x in find_substrings(pattern, layout)] for x in y])
    return set(total_strings)


def find_substrings(pattern, layout):
    pattern_length = len(pattern)
    idx = layout.find(pattern)
    while idx != -1:
        yield [x for x in range(idx, idx+pattern_length)]
        idx = layout.find(pattern, idx+pattern_length)


if __name__ == "__main__":

    patterns, layouts = parse_input('./patterns.dat', './layouts.dat')

    print(task1(patterns, layouts))

