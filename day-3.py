import re

def read_input(filename):
    input = ''
    with open(filename) as f:
        for line in f:
            input += line.strip()
    return input

def find_mul(input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, input)
    return matches

def calculate_1(matches):
    final = []
    for match in matches:
        if 'mul' in match:
            x, y = match.replace('mul(', '').replace(')', '').split(',')
            final.append(int(x) * int(y))
        else:
            pass

    return final

def calculate_2(matches):
    flag = True
    final = []
    for match in matches:
        if 'don\'t' in match:
            flag = False
        elif 'do' in match:
            flag = True
        elif flag and 'mul' in match:
            x, y = match.replace('mul(', '').replace(')', '').split(',')
            final.append(int(x) * int(y))
        else:
            pass

    return final

# input = read_input('./temp.txt')
input = read_input('./input day 3.txt')
# print(input)

matches = find_mul(input)
# print(matches)

result = sum(calculate_2(matches))
print(result)
