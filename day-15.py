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


def move_robot(map, i, j, direction):
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
            map[next_i][next_j] = '@'
            map[i][j] = '.'
            return map, next_i, next_j
        if map[next_i][next_j] == 'O':
            flag = False
            count = 1
            temp_i, temp_j = next_i + \
                directions[direction][0], next_j+directions[direction][1]
            while not flag and temp_i >= 0 and temp_i < len_i and temp_j >= 0 and temp_j < len_j:
                if map[temp_i][temp_j] == '.':
                    flag = True
                    break
                if map[temp_i][temp_j] == '#':
                    break
                temp_i, temp_j = temp_i + \
                    directions[direction][0], temp_j+directions[direction][1]
                count += 1
            if flag:
                map[i][j] = '.'
                map[next_i][next_j] = '@'
                curr_i, curr_j = next_i, next_j
                for _ in range(count):
                    next_i, next_j = next_i + \
                        directions[direction][0], next_j + \
                        directions[direction][1]
                    map[next_i][next_j] = 'O'
                return map, curr_i, curr_j
            return map, i, j


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
        if map[next_i][next_j] == 'O' or map[next_i][next_j] == '@':
            new_map, _, _ = move_robot_v2(copy.deepcopy(
                map), next_i, next_j, direction)
            if new_map[next_i][next_j] == '.':
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
            if map[i][j] == 'O':
                sum += (100*i+j)
    return sum


# map, robot_moves = read_input("./temp.txt")
map, robot_moves = read_input("./input day 15.txt")
print_map(map)
print(robot_moves)


robot_i, robot_j = find_robot(copy.deepcopy(map))
print(robot_i, robot_j)


simulated_map, simulated_i, simulated_j = simulate_movement(
    map, robot_i, robot_j, robot_moves)
print_map(simulated_map)

res_1 = calculate_gps(simulated_map)
print(res_1)
