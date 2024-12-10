def read_input(filename):
    disk_map = ''
    with open(filename) as f:
        disk_map = f.read().strip()
    return disk_map


def create_memory_map(disk_map):
    result = []
    curr_id = -1
    string = ''
    for i in range(len(disk_map)):
        if i % 2 == 0:
            curr_id += 1
            # result += str(curr_id)*int(disk_map[i])
            for j in range(int(disk_map[i])):
                result.append(curr_id)
                string += str(curr_id)

        else:
            # result += '.'*int(disk_map[i])
            for j in range(int(disk_map[i])):
                result.append('.')
                string += '.'
    # print(string)
    return result


def remove_sapce(memory_map):
    i = 0
    j = len(memory_map) - 1
    while i < j:
        if memory_map[i] != '.':
            i += 1
        if memory_map[j] == '.':
            j -= 1
        if memory_map[i] == '.' and memory_map[j] != '.':
            memory_map[i] = memory_map[j]
            memory_map[j] = '.'
            i += 1
            j -= 1
    return memory_map


def remove_sapce_v2(memory_map):
    j = len(memory_map) - 1
    curr_id = memory_map[j]
    curr_id_loc = [j]
    while j > 0:
        j -= 1
        # print(j)
        if curr_id == '.':
            j -= 1
            curr_id = memory_map[j]
        elif memory_map[j] != curr_id and memory_map[j] != '.':
            # print(f'{curr_id} at {curr_id_loc}')
            # moving whole block to left
            for i in range(0, j):
                temp = memory_map[i:i+len(curr_id_loc)]
                # if all(x == '.' for x in temp):
                if ''.join([str(x) for x in temp]) == '.'*len(curr_id_loc):
                    for k in range(len(curr_id_loc)):
                        memory_map[i+k] = curr_id
                        memory_map[curr_id_loc[k]] = '.'
                    break
            curr_id_loc = [j]
            curr_id = memory_map[j]
        elif memory_map[j] == curr_id:
            curr_id_loc.append(j)
        else:
            pass
    return memory_map
# def remove_sapce_v2(memory_map):
#     memory_hash = {}
#     for i in range(len(memory_map)):
#         if memory_map[i] != '.':
#             if memory_map[i] not in memory_hash:
#                 memory_hash[memory_map[i]] = []
#             memory_hash[memory_map[i]].append(i)
#
#     largest = max(memory_hash.keys())
#
#     temp_map = [str(x) for x in memory_map]
#     for i in range(largest, -1, -1):
#         length = len(memory_hash[i])
#         for j in range(len(temp_map)):
#             if ''.join(temp_map[j:j+length]) == '.'*length:
#                 for k in range(length):
#                     temp_map[j+k] = str(i)
#                     temp_map[memory_hash[i][k]] = '.'
#                 break
#     return temp_map


def calculate_checksum(memory_map):
    checksum = 0
    for i in range(len(memory_map)):
        if memory_map[i] != '.':
            checksum += int(memory_map[i])*i
    return checksum


# disk_map = read_input('./temp.txt')
disk_map = read_input('./input day 9.txt')
# print(disk_map)

memory_map = create_memory_map(disk_map)
# print(memory_map)
# print('+'.join([str(x) for x in memory_map]))

# memory_map_space_removed = remove_sapce(list(memory_map))
# print(memory_map_space_removed)
memory_map_space_removed_v2 = remove_sapce_v2(memory_map)
# print(memory_map_space_removed_v2[:300])
# print(''.join([str(x) for x in memory_map_space_removed_v2]))

# checksum = calculate_checksum(memory_map_space_removed)
checksum = calculate_checksum(memory_map_space_removed_v2)
print(checksum)
