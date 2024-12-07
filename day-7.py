def read_input(filename):
    equations = []
    with open(filename) as f:
        for line in f:
            target, values = line.strip().split(":")
            target = int(target.strip())
            values = [int(x.strip()) for x in values.strip().split()]
            equations.append((target, values))
    return equations


def is_valid(target, values):
    # print(target, values)
    if len(values) == 1:
        if target == values[0]:
            return True
        return False
    if (target % values[-1]) == 0 and is_valid((target // values[-1]), values[:-1]):
        return True
    if target > values[-1] and is_valid(target-values[-1], values[:-1]):
        return True
    target_s = str(target)
    last_value_s = str(values[-1])
    if len(target_s) > len(last_value_s) and target_s.endswith(last_value_s) and is_valid(int(target_s[:-len(last_value_s)]), values[:-1]):
        return True
    return False


def check_valid(equations):
    total = 0
    for target, values in equations:
        if is_valid(target, values):
            total += target
    return total


# equations = read_input("./temp.txt")
equations = read_input("./input day 7.txt")
# print(equations)

result_1 = check_valid(equations)
print(result_1)
