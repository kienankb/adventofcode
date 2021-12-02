def part1():
    h = 0
    v = 0
    for line in open('02-01-input.txt', 'r'):
        command = line.split(' ')
        if command[0] == 'forward':
            h += int(command[1])
        elif command[0] == 'down':
            v += int(command[1])
        elif command[0] == 'up':
            v -= int(command[1])
    print(h*v)

def part2():
    h = 0
    v = 0
    a = 0
    for line in open('02-01-input.txt', 'r'):
        command = line.split(' ')
        if command[0] == 'forward':
            amount = int(command[1])
            h += amount
            v += a * amount
        elif command[0] == 'down':
            a += int(command[1])
        elif command[0] == 'up':
            a -= int(command[1])
    print(h*v)

part1()
part2()
