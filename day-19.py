from functools import cache


def read_input(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() != "":
                if ',' in line.strip():
                    result.append([x.strip() for x in line.strip().split(',')])
                else:
                    result.append(line.strip())
    return sorted(result[0], key=len, reverse=True), result[1:]


# def check_possible_towels(towel_available, towels):
#     result = []
#     not_possible = []
#     for towel in towels:
#         print(towel)
#         temp = towel
#         for t in towel_available:
#             if t in temp:
#                 temp = temp.replace(t, '')
#                 print(towel, temp, t)
#         if len(temp) == 0:
#             result.append(towel)
#         else:
#             not_possible.append(towel)
#     print(len(result))
#     # print(not_possible)
#
@cache
def check_possible(towel):
    maxlen = len(towel_available[0])
    if towel == "":
        return True
    for i in range(min(len(towel), maxlen)+1):
        if towel[:i] in towel_available and check_possible(towel[i:]):
            return True
    return False


@cache
def check_possible2(towel):
    maxlen = len(towel_available[0])
    if towel == "":
        return 1
    count = 0
    for i in range(min(len(towel), maxlen)+1):
        if towel[:i] in towel_available:
            count += check_possible2(towel[i:])
    return count


def check_possible_towels(towels):
    count = 0
    for towel in towels:
        temp = check_possible2(towel)
        # print(temp)
        if temp:
            count += temp
            # print(towel, temp)
    print(count)


global towel_available
# towel_available, towels = read_input('./temp.txt')
towel_available, towels = read_input('./input day 19.txt')
# print(towel_available)

check_possible_towels(towels)
