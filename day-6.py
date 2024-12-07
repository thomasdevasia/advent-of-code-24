import copy

def read_input(filename):
    grid = []
    with open (filename, 'r') as f:
        for line in f:
            grid.append([x for x in line.strip()])
    return grid

def find_start(grid):
    flag = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                flag = True
                break
        if flag:
            break
    
    return i, j

def print_grid(grid):
    for g in grid:
        print(''.join(g))
    print('---------------------------------')

def find_end(grid, start_x, start_y):
    
    curr = 'T'
    move = {
        'T': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    len_x = len(grid)
    len_y = len(grid[0])

    x = start_x
    y = start_y
    
    seen = set()
    # seen.add((x, y, curr))

    while (x >= 0 and x < len_x and y >= 0 and y < len_y):
        # print(x, y)
        if grid[x][y] == '#':
            # print('equal')
            x -= move[curr][0]
            y -= move[curr][1]
            if curr == 'T':
                curr = 'R'
            elif curr == 'R':
                curr = 'D'
            elif curr == 'D':
                curr = 'L'
            elif curr == 'L':
                curr = 'T'
            else:
                pass
        grid[x][y] = 'X'
        if (x, y, curr) not in seen:
            seen.add((x, y))
            # print(x, y, curr)
            # print_grid(grid)
        # print_grid(grid)
        x += move[curr][0]
        y += move[curr][1]
        
    return grid, seen

def check_loop(grid, start_x, start_y):
    curr = 'T'
    move = {
        'T': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    len_x = len(grid)
    len_y = len(grid[0])
    x = start_x
    y = start_y
    seen = set()

    flag = False

    while (x >= 0 and x < len_x and y >= 0 and y < len_y):
        if grid[x][y] == '#' or grid[x][y] == 'O':
            x -= move[curr][0]
            y -= move[curr][1]
            if curr == 'T':
                curr = 'R'
            elif curr == 'R':
                curr = 'D'
            elif curr == 'D':
                curr = 'L'
            elif curr == 'L':
                curr = 'T'
            else:
                pass
        if (x, y, curr) in seen:
            flag = True
            break
        seen.add((x, y, curr))
        x += move[curr][0]
        y += move[curr][1]
    
    # if flag:
    #     print_grid(grid)
    return flag

def create_loop(grid, seen_paths, start_x, start_y):
    total = 0
    print(len(seen_paths))
    for path in seen_paths:
        new_grid = copy.deepcopy(grid)
        new_grid[path[0]][path[1]] = 'O'
        # print_grid(new_grid)
        total += check_loop(new_grid, start_x, start_y)
    print('Total:', total)


def calculate_path(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'X':
                total += 1
    return total

# grid = read_input('./temp.txt')
grid = read_input('./input day 6.txt')
# print_grid(grid)

start_x, start_y = find_start(grid)
# print(start_x, start_y)

new_grid, seen_paths = find_end(grid, start_x, start_y)
# print_grid(new_grid)
# print(len(seen_paths))

result_1 = calculate_path(new_grid)
print('Result:', result_1)


total_loops = create_loop(grid, seen_paths, start_x, start_y)
