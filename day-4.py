import re

def read_input(file_path):
    input = []
    with open(file_path) as f:
        for line in f:
            input.append([x for x in line.strip()])

    return input

def check_word(input, i, j, word):
    word_len = len(word)-1
    j_len = len(input[0])
    i_len = len(input)
    sum = 0

    def check_horizontal_right(i, j, word):
        if j + word_len < j_len:
            temp = input[i][j:j+word_len+1]
            print(''.join(temp))
            if temp == word:
                return True
        return False
    def check_horizontal_left(i, j, word):
        if j - word_len >= 0:
            temp = input[i][j-word_len:j+1]
            print(''.join(temp))
            if temp == word:
                return True
        return False
    def check_vertical_down(i, j, word):
        if i + word_len < i_len:
            temp = [input[x][j] for x in range(i, i+word_len+1)]
            print(''.join(temp))
            if temp == word:
                return True
        return False
    def check_vertical_up(i, j, word):
        if i - word_len >= 0:
            temp = [input[x][j] for x in range(i-word_len, i+1)]
            print(''.join(temp))
            if temp == word:
                return True
        return False
    
    sum += check_horizontal_right(i,j,word)
    sum += check_horizontal_left(i,j,word)
    sum += check_vertical_down(i,j,word)
    sum += check_vertical_up(i,j,word)

    # def check_diagonal_down_right(i, j, word):
    #     if i + word_len < i_len or j + word_len < j_len:
    # def check_diagonal_down_left(i, j, word):
    #     if i + word_len < i_len or j - word_len >= 0:
    # def check_diagonal_up_right(i, j, word):
    #     if i - word_len >= 0 or j + word_len < j_len:
    # def check_diagonal_up_left(i, j, word):
    #     if i - word_len >= 0 or j - word_len >= 0:

def find_word(input, word):
    start_letter = word[0]
    result = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][0] == start_letter:
                temp = check_word(input, i, j, word)
                if temp:
                    result += temp
    return result
    
input = read_input('./temp.txt')
# print(input)

result = find_word(input, 'XMAS')
