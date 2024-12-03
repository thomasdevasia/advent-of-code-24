def read_input(filename):
    reports = []
    with open(filename) as f:
        for line in f:
            reports.append([int(x) for x in line.strip().split()])
    return reports

def check_safety(reports):
    result = []
    for report in reports:
        diff = [report[i]-report[i+1] for i in range(len(report)-1)]
        print(report)
        print(diff)
        print('------------------')

        if all(x > 0 and x <= 3 for x in diff):
            result.append(1)
        elif all(x < 0 and x >= -3 for x in diff):
            result.append(1)
        else:
            result.append(0)
    # return result
    return sum(result)

# def check_safety_with_dampener(reports):

reports = read_input("temp.txt")
# print(reports)

result = check_safety(reports)
print(result)
