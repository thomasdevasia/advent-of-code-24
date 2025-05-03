from copy import deepcopy


def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            result.append(line.strip())
    return result


def print_maze(maze):
    for row in maze:
        print(''.join(row))


maze = read_input("./temp.txt")
print_maze(maze)
