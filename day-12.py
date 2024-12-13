def read_input(filename):
    farm = []
    with open(filename) as f:
        for line in f:
            farm.append([x for x in line.strip()])
    return farm


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def calculate_price(farm):
    farm_passed = []
    len_row = len(farm)
    len_col = len(farm[0])
    count = 0
    perimeter = 0
    farm_names = {}

    def walk(r, c, farm, len_row, len_col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        nonlocal perimeter, count
        # print(f"r: {r}, c: {c} = {farm[r][c]}")
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            # print(f"nr: {nr}, nc: {nc}")
            if nr < 0 or nc < 0 or nr >= len_row or nc >= len_col:
                perimeter += 1
            elif farm[nr][nc] != farm[r][c]:
                perimeter += 1

        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            if (nr, nc) not in farm_passed and nr >= 0 and nc >= 0 and nr < len_row and nc < len_col:
                if farm[nr][nc] == farm[r][c]:
                    farm_passed.append((nr, nc))
                    count += 1
                    walk(nr, nc, farm, len_row, len_col)

    for r in range(len(farm)):
        for c in range(len(farm[r])):
            if (r, c) not in farm_passed:
                if (r, c) not in farm_passed:
                    perimeter = 0
                    count = 1
                    farm_passed.append((r, c))
                    walk(r, c, farm, len_row, len_col)
                    # print(f"Perimeter of farm {farm[r][c]} is {perimeter}")
                if farm[r][c] in farm_names:
                    farm_names[farm[r][c]].append((count, perimeter))
                else:
                    farm_names[farm[r][c]] = [(count, perimeter)]

    # print(farm_names)

    total_price = 0
    for farm_name in farm_names:
        total_price += sum([x[0] * x[1] for x in farm_names[farm_name]])

    print(f"Total price: {total_price}")


def find_corner(r, c, farm, len_row, len_col):
    corner = 0
    top = False
    bottom = False
    left = False
    right = False
    curr = farm[r][c]
    if r-1 < 0 or farm[r-1][c] != farm[r][c]:
        top = True
    if r+1 >= len_row or farm[r+1][c] != farm[r][c]:
        bottom = True
    if c-1 < 0 or farm[r][c-1] != farm[r][c]:
        left = True
    if c+1 >= len_col or farm[r][c+1] != farm[r][c]:
        right = True

    if top and left:
        corner += 1
    if top and right:
        corner += 1
    if bottom and left:
        corner += 1
    if bottom and right:
        corner += 1

    # TO DO: check the corners
    # if r-1 < 0 and c-1 < 0:
    #     top_left = farm[r-1][c-1]
    # else:
    #     top_left = False
    # if r-1 >= 0 and c+1 > len_col:
    #     top_right = farm[r-1][c+1]
    # else:
    #     top_right = False
    # if r+1 > len_row and c-1 < 0:
    #     bottom_left = farm[r+1][c-1]
    # else:
    #     bottom_left = False
    # if r+1 > len_row and c+1 > len_col:
    #     bottom_right = farm[r+1][c+1]
    # else:
    #     bottom_right = False
    # if top_left == curr and left:
    #     corner += 1
    # if top_right == curr and top:
    #     corner += 1
    # if bottom_left == curr and left:
    #     corner += 1
    # if bottom_right == curr and right:
    #     corner += 1

    return corner


def calculate_price_v2(farm):
    farm_passed = []
    len_row = len(farm)
    len_col = len(farm[0])
    count = 0
    perimeter = 0
    farm_names = {}

    def walk(r, c, farm, len_row, len_col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        nonlocal perimeter, count
        # print(f"r: {r}, c: {c} = {farm[r][c]}")
        perimeter += find_corner(r, c, farm, len_row, len_col)
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            if (nr, nc) not in farm_passed and nr >= 0 and nc >= 0 and nr < len_row and nc < len_col:
                if farm[nr][nc] == farm[r][c]:
                    farm_passed.append((nr, nc))
                    count += 1
                    walk(nr, nc, farm, len_row, len_col)

    for r in range(len(farm)):
        for c in range(len(farm[r])):
            if (r, c) not in farm_passed:
                if (r, c) not in farm_passed:
                    perimeter = 0
                    count = 1
                    farm_passed.append((r, c))
                    walk(r, c, farm, len_row, len_col)
                    # print(f"Perimeter of farm {farm[r][c]} is {perimeter}")
                if farm[r][c] in farm_names:
                    farm_names[farm[r][c]].append((count, perimeter))
                else:
                    farm_names[farm[r][c]] = [(count, perimeter)]

    print(farm_names)

    total_price = 0
    for farm_name in farm_names:
        total_price += sum([x[0] * x[1] for x in farm_names[farm_name]])

    print(f"Total price: {total_price}")


farm = read_input("./temp.txt")
# farm = read_input("./input day 12.txt")
print_matrix(farm)

# total_price = calculate_price(farm)
total_price = calculate_price_v2(farm)
