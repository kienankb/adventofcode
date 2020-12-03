def intcode(instructions):
    halt = False
    pointer = 0
    while not halt:
        if instructions[pointer] == 1:
            instructions[instructions[pointer+3]] = instructions[instructions[pointer+1]] + instructions[instructions[pointer+2]]
        elif instructions[pointer] == 2:
            instructions[instructions[pointer+3]] = instructions[instructions[pointer+1]] * instructions[instructions[pointer+2]]
        elif instructions[pointer] == 99:
            halt = True
        else:
            raise Exception
        pointer += 4
    return instructions[0]

def loadInstructions():
    instructions = open('01-input.txt').read().strip().split(',')
    instructions = [int(x) for x in instructions]
    return instructions

def part1():
    instructions = loadInstructions()
    # oh shit, 1202 error
    instructions[1] = 12
    instructions[2] = 2
    return intcode(instructions)

def part2():
    result = 0
    noun = 0
    verb = 0
    while True:
        instructions = loadInstructions()
        instructions[1] = noun
        instructions[2] = verb
        result = intcode(instructions)
        if result == 19690720:
            print(100 * noun + verb)
            break
        if verb == 99:
            verb = 0
            noun += 1
        else:
            verb += 1

if __name__ == '__main__':
    print(part1())
    part2()