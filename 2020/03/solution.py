def part1(over=3, down=1):
    with open('./03-input.txt', 'r') as inFile:
        terrain = [line.strip() for line in inFile]
    level = 0
    encounteredTrees = 0
    horizontalPosition = 0
    while level < len(terrain):
        if terrain[level][horizontalPosition % len(terrain[level])] == '#':
            encounteredTrees += 1
        horizontalPosition += over
        level += down
    return encounteredTrees

def part2():
    return part1(over=1)*part1()*part1(over=5)*part1(over=7)*part1(over=1,down=2)

print(part1())
print(part2())
