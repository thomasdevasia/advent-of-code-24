import re


def read_input(filename):
    with open(filename) as f:
        res = [{}]
        count = 0
        for n, line in enumerate(f):
            line = line.strip()
            if n % 4 == 0:
                match = re.search(r"X\+(\d+), Y\+(\d+)", line)
                x = int(match.group(1))
                y = int(match.group(2))
                res[count]["A"] = (x, y)
            elif n % 4 == 1:
                match = re.search(r"X\+(\d+), Y\+(\d+)", line)
                x = int(match.group(1))
                y = int(match.group(2))
                res[count]["B"] = (x, y)
            elif n % 4 == 2:
                match = re.search(r"X=(\d+), Y=(\d+)", line)
                x = int(match.group(1))
                y = int(match.group(2))
                # res[count]["prize"] = (x, y)
                res[count]["prize"] = (x+10000000000000, y+10000000000000)
            else:
                res.append({})
                count += 1
    return res

# using linear equation to solve


def solve(machines):
    total = 0
    for machine in machines:

        a_press = ((machine["prize"][0]*machine["B"][1]) - (machine["prize"][1]*machine["B"][0])
                   ) / ((machine["A"][0]*machine["B"][1]) - (machine["A"][1]*machine["B"][0]))
        # printing the equation
        # print(f"{machine['prize'][0]}*{machine['B'][1]} - {machine['prize'][1]}*{machine['A']
        #                                                                          [0]} / {machine['A'][0]}*{machine['B'][1]} - {machine['A'][1]}*{machine['B'][0]} = {a_press}")
        b_press = (machine["prize"][0]-machine["A"]
                   [0]*a_press) / machine["B"][0]
        # print(f"{machine['prize'][0]} - {machine['A']
        #                                  [0]}*{a_press} / {machine['B'][0]}= {b_press}")
        # print(a_press, b_press)
        if a_press.is_integer() and b_press.is_integer():
            total += a_press * 3 + b_press
    return total


# machines = read_input("./temp.txt")
machines = read_input("./input day 13.txt")
# print(machines)

total_token = solve(machines)
print(total_token)
