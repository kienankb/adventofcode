def part1():
    with open('./03-input.txt', 'r') as inFile:
        terrain = [line.strip() for line in inFile]
    encounteredTrees = 0
    horizontalPosition = 0
    for level in terrain:
        if level[horizontalPosition % len(level)] == '#':
            encounteredTrees += 1
        horizontalPosition += 3
    return encounteredTrees

def part2():
    pass

print(part1())
print(part2())
