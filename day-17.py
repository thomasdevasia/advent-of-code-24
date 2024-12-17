def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            if line.strip() != '':
                result.append(line.strip().split(' ')[-1])
    return int(result[0]), int(result[1]), int(result[2]), [int(x) for x in result[3].split(',')]


def combo_opernand(operand, register_a, register_b, register_c):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return register_a
    elif operand == 5:
        return register_b
    elif operand == 6:
        return register_c
    else:
        pass


def execute(register_a, register_b, register_c, program):
    instruction_pointer = 0
    result = []
    while (instruction_pointer < len(program)):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        print(f'Opcode: {opcode} Operand: {operand}')
        if opcode == 0:
            temp = register_a//(2**combo_opernand(operand,
                                register_a, register_b, register_c))
            register_a = temp
        elif opcode == 1:
            temp = register_b ^ operand
            register_b = temp
        elif opcode == 2:
            temp = combo_opernand(operand, register_a,
                                  register_b, register_c) % 8
            register_b = temp
        elif opcode == 3:
            if register_a != 0:
                instruction_pointer = operand
            else:
                instruction_pointer += 2
        elif opcode == 4:
            temp = register_c ^ register_b
            register_b = temp
        elif opcode == 5:
            temp = combo_opernand(operand, register_a,
                                  register_b, register_c) % 8
            result.append(temp)
        elif opcode == 6:
            temp = register_a//(2**combo_opernand(operand,
                                register_a, register_b, register_c))
            register_b = temp
        elif opcode == 7:
            temp = register_a//(2**combo_opernand(operand,
                                register_a, register_b, register_c))
            register_c = temp
        else:
            print('Invalid opcode')
        if opcode != 3:
            instruction_pointer += 2

    print('='*20)
    print(f'New Register A: {register_a}')
    print(f'New Register B: {register_b}')
    print(f'New Register C: {register_c}')
    print(f'Result: {result}')
    return result


# register_a, register_b, register_c, program = read_input('./temp.txt')
register_a, register_b, register_c, program = read_input('./input day 17.txt')
print(f'Register A: {register_a}')
print(f'Register B: {register_b}')
print(f'Register C: {register_c}')
print(f'Program: {program}')

output = execute(register_a, register_b, register_c, program)
print(','.join([str(x) for x in output]))
