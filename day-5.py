def read_input(filename):
    page_order_rules = []
    flag = False
    updates = []
    with open (filename, 'r') as f:
        for line in f:
            if line.strip() == '':
                flag = True
            else:
                if flag:
                    updates.append([int(x) for x in line.strip().split(',')])
                else:
                    page_order_rules.append(line.strip())
    return page_order_rules, updates

def create_map(page_order_rules):
    page_rule_map = {}
    for rule in page_order_rules:
        temp = [int(x) for x in rule.split('|')]
        if temp[1] not in page_rule_map:
            page_rule_map[temp[1]] = []
        page_rule_map[temp[1]].append(temp[0])
    return page_rule_map

def check_updates(page_rule_map, updates):
    correct_list = []
    incorrect_list = []
    for update in updates:
        flag = False
        # print(update)
        for i in range(len(update)-1):
            if update[i] in page_rule_map:
                rule = page_rule_map[update[i]]
                # print(update[i], rule)
                for item in update[i+1:]:
                    # print(item, rule)
                    if item in rule:
                        flag = True
                        # print('flag', flag)
                        break
                if flag:
                    break
        if not flag:
            correct_list.append(update)
        else:
            incorrect_list.append(update)
    # print(correct_list)

    total = 0
    for item in correct_list:
        mid = item[len(item)//2]
        total += int(mid)

    return total, incorrect_list

def sort_list(unsorted_list, page_rule_map):
    for i in range(len(unsorted_list)):
        if unsorted_list[i] in page_rule_map:
            # TODO: 'sort the list'


page_order_rules, updates = read_input('./temp.txt')
# page_order_rules, updates = read_input('./input day 5.txt')
# print(page_order_rules)
# print(updates)

page_rule_map = create_map(page_order_rules)
# print(page_rule_map)

correct_list_total, incorrect_list = check_updates(page_rule_map, updates)
print(correct_list_total)
print(incorrect_list)
