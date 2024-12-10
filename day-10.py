def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            result.append([int(x) for x in line.strip()])
    return result


def print_map(topographic_map):
    for row in topographic_map:
        print("".join([str(x) for x in row]))


def find_9(r, c, topographic_map):
    res = []
    # top
    if r-1 >= 0 and topographic_map[r-1][c] == topographic_map[r][c] + 1:
        if topographic_map[r-1][c] == 9:
            res.append((r-1, c))
        else:
            res += find_9(r-1, c, topographic_map)
    # down
    if r+1 < len(topographic_map) and topographic_map[r+1][c] == topographic_map[r][c] + 1:
        if topographic_map[r+1][c] == 9:
            res.append((r+1, c))
        else:
            res += find_9(r+1, c, topographic_map)
    # left
    if c-1 >= 0 and topographic_map[r][c-1] == topographic_map[r][c]+1:
        if topographic_map[r][c-1] == 9:
            res.append((r, c-1))
        else:
            res += find_9(r, c-1, topographic_map)
    # right
    if c+1 < len(topographic_map[0]) and topographic_map[r][c+1] == topographic_map[r][c]+1:
        if topographic_map[r][c+1] == 9:
            res.append((r, c+1))
        else:
            res += find_9(r, c+1, topographic_map)
    # return list(set(res))
    return res


def calculate_score(topographic_map):
    score = 0
    for r in range(len(topographic_map)):
        for c in range(len(topographic_map[0])):
            if topographic_map[r][c] == 0:
                temp = find_9(r, c, topographic_map)
                # print(temp, len(temp))
                score += len(list(set(temp)))
    return score


def calculate_score_v2(topographic_map):
    score = 0
    for r in range(len(topographic_map)):
        for c in range(len(topographic_map[0])):
            if topographic_map[r][c] == 0:
                temp = find_9(r, c, topographic_map)
                # print(temp, len(temp))
                score += len(temp)
    return score


# topographic_map = read_input("./temp.txt")
topographic_map = read_input("./input day 10.txt")
print_map(topographic_map)


result_v1 = calculate_score(topographic_map)
print(result_v1)
result_v2 = calculate_score_v2(topographic_map)
print(result_v2)
