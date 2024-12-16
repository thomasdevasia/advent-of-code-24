from copy import deepcopy


def read_input(filename):
    res = []
    with open(filename) as f:
        for line in f:
            res.append([x for x in line.strip()])
    return res


def print_maze(maze):
    for row in maze:
        print("".join(row))


def print_maze_solutions(maze, solution):
    res = []
    for i in range(len(maze)):
        temp = []
        for j in range(len(maze[0])):
            if (i, j) in solution:
                temp.append("X")
            else:
                temp.append(maze[i][j])
        res.append(temp)
    print('='*25)
    print_maze(res)
    print('='*25)


cur_path = []
passed_path = set()
solutions = []


def move(maze, r, c, toatal_available_path):
    len_row = len(maze)
    len_col = len(maze[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if len(passed_path) == toatal_available_path:
        return False
    if maze[r][c] == "E":
        solutions.append(deepcopy(cur_path))
        return False
    for direction in directions:
        nr = r + direction[0]
        nc = c + direction[1]
        if nr >= 0 and nc >= 0 and nr < len_row and nc < len_col and maze[nr][nc] != "#" and (nr, nc) not in cur_path:
            cur_path.append((r, c))
            # print_maze_solutions(maze)
            passed_path.add((r, c))
            move(maze, nr, nc, toatal_available_path)
            cur_path.pop()


def solve_maze(maze):
    len_row = len(maze)
    start = (len_row-2, 1)
    temp_maze = deepcopy(maze)
    toatal_available_path = sum(
        [True for row in maze for cell in row if cell == "."])
    move(temp_maze, start[0], start[1], toatal_available_path)
    # print(solutions)
    # for solution in solutions:
    #     print('='*25)
    #     print_maze_solutions(maze, solution)
    #     print('='*25)
    print(len(solutions))
    solution_scores = []
    for solution in solutions:
        prev = solution[0]
        curr_dir = (0, 0)
        temp_score = 0
        for s in solution[1:]:
            diff = (s[0] - prev[0], s[1] - prev[1])
            # print(prev, s, diff)
            if curr_dir == diff:
                temp_score += 1
            else:
                temp_score += 1001
                curr_dir = diff
            prev = s
        solution_scores.append(temp_score+1)
        # if temp_score == 7028:
        #     print_maze_solutions(maze, solution)
    solution_scores.sort()
    print(solution_scores)


if __name__ == "__main__":
    # maze = read_input("./temp.txt")
    maze = read_input("./input day 16.txt")
    print_maze(maze)

    solved_paths = solve_maze(maze)
