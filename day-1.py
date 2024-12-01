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

# sorting left list
left_list.sort()

# sortinng right list
right_list.sort()

distance_list = []

for i in range(len(left_list)):
    distance = abs(left_list[i] - right_list[i])
    distance_list.append(distance)

total_distance = sum(distance_list)
print(total_distance)
