from copy import deepcopy
from collections import deque


def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            temp = line.strip().split(',')
            result.append((int(temp[1]), int(temp[0])))
    return result


def create_map(s, corrupted_cords, steps):
    result = []
    for i in range(s):
        result.append(['.' for _ in range(s)])
    for r, c in corrupted_cords[:steps]:
        result[r][c] = '#'
    return result


def print_map(m):
    for row in m:
        print(''.join(row))


def find_path(ram_map):
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    len_r = len(ram_map)
    len_c = len(ram_map[0])
    flag = False
    while q:
        r, c, d = q.popleft()
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < len_r and 0 <= nc < len_c and (nr, nc) not in seen and ram_map[nr][nc] == '.':
                if (nr, nc) == (len_r-1, len_c-1):
                    # print(d+1)
                    flag = True
                    break
                q.append((nr, nc, d+1))
                seen.add((nr, nc))
        if flag:
            break
    return flag


def cheeck_bytes(s, corrupted_cords):
    lo = 0
    high = len(corrupted_cords)-1
    while lo < high:
        mid = (lo+high)//2
        ram_map = create_map(s+1, corrupted_cords, mid)
        if find_path(ram_map):
            lo = mid+1
        else:
            high = mid
    print(corrupted_cords[lo-1])


# corrupted_cords = read_input('./temp.txt')
# cheeck_bytes(6, corrupted_cords)
corrupted_cords = read_input('./input day 18.txt')
cheeck_bytes(70, corrupted_cords)
