import os

left_list = []
right_list = []

with open('./input day 1.txt') as input_file:
    data = input_file.read()
    temp = data.split()
    for i in range(len(temp)):
        if i%2 == 0:
            left_list.append(int(temp[i]))
        else:
            right_list.append(int(temp[i]))

# left_list = [3,4,2,1,3,3]
# right_list = [4,3,5,3,9,3]

temp_hash = {}
for i in range(len(right_list)):
    if right_list[i] in temp_hash:
        temp_hash[right_list[i]] += 1
    else:
        temp_hash[right_list[i]] = 1

total_similarity = 0
for val in left_list:
    if val in temp_hash:
        total_similarity += (val * temp_hash[val])

print(total_similarity)
