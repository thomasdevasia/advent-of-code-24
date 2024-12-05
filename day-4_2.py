def read_input(file_path):
    input = []
    with open(file_path) as f:
        input = f.read().splitlines()

    return input

# def find_word(input):
#     sum = 0
#     temp = ''
#     for i in range(len(input)):
#         for j in range(len(input[i])):
#             try:
#                 if input[i][j] == 'A':
#                     # print(i, j)
#                     # print(input[i-1][j-1],  input[i-1][j+1], input[i+1][j-1], input[i+1][j+1])
#                     temp += f'{input[i-1][j-1]} {input[i-1][j+1]} {input[i+1][j-1]} {input[i+1][j+1]}\n'
#                     if input[i-1][j-1] == 'M' and input[i-1][j+1]=='S' and input[i+1][j-1]=='M' and input[i+1][j+1]=='S':
#                         sum += 1
#                     elif input[i-1][j-1] == 'M' and input[i-1][j+1]=='M' and input[i+1][j-1]=='S' and input[i+1][j+1]=='S':
#                         sum += 1
#                     elif input[i-1][j-1] == 'S' and input[i-1][j+1]=='S' and input[i+1][j-1]=='M' and input[i+1][j+1]=='M':
#                         sum += 1
#                     elif input[i-1][j-1] == 'S' and input[i-1][j+1]=='M' and input[i+1][j-1]=='S' and input[i+1][j+1]=='M':
#                         sum += 1
#                     else:
#                         pass
#                     # print(sum)
#                     temp += f'{sum}\n'
#             except:
#                 pass
#     with open('./temp2.txt', 'w') as f:
#         f.write(temp)
#     return sum
#
def find_word(input):
    sum = 0
    for i in range(1, len(input)-1):
        for j in range(1, len(input[i])-1):
            if input[i][j] == 'A':
                try:
                    corners = [input[i-1][j-1],  input[i-1][j+1], input[i+1][j+1], input[i+1][j-1]]
                    if ''.join(corners) in ['MMSS', 'MSSM', 'SSMM', 'SMMS']:
                        sum += 1
                except:
                    pass
    return sum

input = read_input('./input day 4.txt')
# input = read_input('temp.txt')
# print(input)

result = find_word(input)
print(result)

