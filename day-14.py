from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os
import sys
import re


def read_input(filename):
    res = []
    pattern = r"p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)"
    with open(filename) as f:
        for line in f:
            match = re.match(pattern, line.strip())
            # print(line.strip())
            px, py, vx, vy = map(int, match.groups())
            # print(px, py, vx, vy)
            res.append((px, py, vx, vy))
    return res


def create_matrix(width, height):
    return [["." for _ in range(width)] for _ in range(height)]


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def simulated_map(robots, matrix):
    for robot in robots:
        x, y = robot
        if matrix[y][x] == ".":
            matrix[y][x] = "1"
        else:
            matrix[y][x] = "2"
    return matrix


def move_robot(robot, matrix, n):
    len_x = len(matrix[0])
    len_y = len(matrix)
    x, y, vx, vy = robot
    current_x = (x + vx * n) % len_x
    if current_x < 0:
        current_x = len_x + current_x
    current_y = (y + vy * n) % len_y
    if current_y < 0:
        current_y = len_y + current_y
    return current_x, current_y


def simulate(robots, matrix, n):
    current = []
    for robot in robots:
        current_x, current_y = move_robot(robot, matrix, n)
        current.append((current_x, current_y))
    # return current
    return simulated_map(current, matrix)


def calculate_safety_factor(matrix):
    middle_x = len(matrix[0]) // 2
    middle_y = len(matrix) // 2
    q1, q2, q3, q4 = 0, 0, 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "." and i != middle_y and j != middle_x:
                if i < middle_y and j < middle_x:
                    q1 += int(matrix[i][j])
                elif i < middle_y and j >= middle_x:
                    q2 += int(matrix[i][j])
                elif i >= middle_y and j < middle_x:
                    q3 += int(matrix[i][j])
                else:
                    q4 += int(matrix[i][j])
    # print(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4


def plot_matrix_graph(matrix, n):
    points = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value != '.':
                try:
                    # Add (x, y, value) to points
                    points.append((j, i, float(value)))
                except ValueError:
                    print(f"Skipping invalid value at ({i}, {j}): {value}")

    if not points:
        print("No valid points to plot.")
        return

    # Ensure the output directory exists
    os.makedirs('./image', exist_ok=True)

    # Create the plot
    x, y, values = zip(*points)
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(x, y, c=values, cmap='viridis', edgecolors='k')
    plt.colorbar(scatter, label='Values')
    plt.title('Matrix Graph')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().invert_yaxis()  # Flip the y-axis so (0,0) is top-left
    plt.grid(True, linestyle='--', alpha=0.7)

    # Save the image
    output_path = f'./image/simulation_graph_{n}.png'
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Graph saved to {output_path}")


def matrix_to_image(matrix, n):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Create a new blank image with white background
    img = Image.new("RGB", (cols, rows), "white")
    draw = ImageDraw.Draw(img)

    # Fill pixels based on matrix values
    for y in range(rows):
        for x in range(cols):
            if matrix[y][x] != '.':
                draw.point((x, y), fill="black")

    # Save the image
    output_file = f'./image/simulation_{n}.png'
    img.save(output_file)
    print(f"Image saved as {output_file}")

# robots = read_input("./temp.txt")
# matrix = create_matrix(11, 7)
# simulations = simulate(robots, matrix, 100)
# print_matrix(simulations)
# safety_factor = calculate_safety_factor(simulations)
# print(safety_factor)


robots = read_input("./input day 14.txt")
# matrix = create_matrix(101, 103)
# simulations = simulate(robots, matrix, 100)
# print_matrix(simulations)
# safety_factor = calculate_safety_factor(simulations)
# print(safety_factor)

# start = int(sys.argv[1])
# end = int(sys.argv[2])
lowest_sf = float("inf")
lowest_n = 0
# 6752
for i in range(0, 100000):
    matrix = create_matrix(101, 103)
    simulations = simulate(robots, matrix, i)
    # plot_matrix_graph(simulations, i)
    # matrix_to_image(simulations, i)
    safety_factor = calculate_safety_factor(simulations)
    # print(i)
    if lowest_sf > safety_factor:
        lowest_sf = safety_factor
        lowest_n = i
print(lowest_sf, lowest_n)
