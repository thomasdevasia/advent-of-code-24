import copy


def read_input(filename):
    map = []
    robot_moves = ''
    with open(filename) as f:
        for line in f:
            if line.strip() != '':
                if line.startswith('#'):
                    map.append([x for x in line.strip()])
                else:
                    robot_moves += line.strip()
    return map, robot_moves


def print_map(map):
    for line in map:
        print(''.join(line))


def find_robot(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '@':
                break
        if map[i][j] == '@':
            break
    return i, j


def enlarge_map(map):
    new_map = []
    for i in range(len(map)):
        temp = []
        for j in range(len(map[i])):
            if map[i][j] == '#':
                temp.append('#')
                temp.append('#')
            elif map[i][j] == '.':
                temp.append('.')
                temp.append('.')
            elif map[i][j] == 'O':
                temp.append('[')
                temp.append(']')
            elif map[i][j] == '@':
                temp.append('@')
                temp.append('.')
        new_map.append(temp)
    return new_map


def move_robot_v2(map, i, j, direction):
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    next_i, next_j = i + directions[direction][0], j + directions[direction][1]
    len_i, len_j = len(map), len(map[0])
    if next_i >= 0 and next_i < len_i and next_j >= 0 and next_j < len_j:
        if map[next_i][next_j] == '#':
            return map, i, j
        if map[next_i][next_j] == '.':
            map[next_i][next_j] = map[i][j]
            map[i][j] = '.'
            return map, next_i, next_j
        if map[next_i][next_j] == '[' or map[next_i][next_j] == ']' or map[next_i][next_j] == '@':
            new_map, _, _ = move_robot_v2(copy.deepcopy(
                map), next_i, next_j, direction)
            if new_map[next_i][next_j] == '.':
                # if (direction == '^' or direction == 'v') and map[next_i][next_j] == ']' and map[next_i][next_j] == '[':
                if (direction == '^' or direction == 'v') and (map[next_i][next_j] == ']' or map[next_i][next_j] == '['):
                    # print_map(new_map)
                    # pass
                    if map[next_i][next_j] == '[':
                        new_map, _, _ = move_robot_v2(copy.deepcopy(
                            new_map), next_i, next_j+1, direction)
                        if new_map[next_i][next_j+1] == '.':
                            new_map[next_i][next_j] = map[i][j]
                            new_map[i][j] = '.'
                            # print_map(new_map)
                            return new_map, next_i, next_j
                    elif map[next_i][next_j] == ']':
                        new_map, _, _ = move_robot_v2(copy.deepcopy(
                            new_map), next_i, next_j-1, direction)
                        if new_map[next_i][next_j-1] == '.':
                            new_map[next_i][next_j] = map[i][j]
                            new_map[i][j] = '.'
                            # print_map(new_map)
                            return new_map, next_i, next_j
                else:
                    new_map[next_i][next_j] = map[i][j]
                    new_map[i][j] = '.'
                    return new_map, next_i, next_j
    return map, i, j


def simulate_movement(map, robtor_i, robot_j, directions):
    curr_map = copy.deepcopy(map)
    curr_i, curr_j = robtor_i, robot_j
    for direction in directions:
        # print_map(curr_map)
        # print(direction)
        curr_map, curr_i, curr_j = move_robot_v2(
            curr_map, curr_i, curr_j, direction)
    return curr_map, curr_i, curr_j


def calculate_gps(map):
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '[':
                sum += 100*i+j
    return sum


# map, robot_moves = read_input("./temp.txt")
map, robot_moves = read_input("./input day 15.txt")
print_map(map)
print(robot_moves)
enlarged_map = enlarge_map(copy.deepcopy(map))
print_map(enlarged_map)
robot_i, robot_j = find_robot(copy.deepcopy(enlarged_map))
print(robot_i, robot_j)
simulated_map, simulated_i, simulated_j = simulate_movement(
    enlarged_map, robot_i, robot_j, robot_moves)
print_map(simulated_map)
res = calculate_gps(simulated_map)
print(res)
