def part1():
    depths = []
    increases = 0
    for line in open('01-01-input.txt', 'r'):
        depths.append(int(line))
    for i in range(len(depths) - 1):
        if depths[i] < depths[i+1]:
            increases += 1
    print(increases)

def part2():
    depths = []
    sums = []
    increases = 0
    for line in open('01-01-input.txt', 'r'):
        depths.append(int(line))
    while len(depths) >= 3:
        sums.append(depths[0]+depths[1]+depths[2])
        depths.pop(0)
    for i in range(len(sums) - 1):
        if sums[i] < sums[i+1]:
            increases += 1
    print(increases)

part1()
part2()
