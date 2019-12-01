import math

def part1():
    totalFuel = 0
    for moduleMass in open('01-input.txt'):
        fuel = math.floor(int(moduleMass)/3)-2
        totalFuel += fuel
    return totalFuel

if __name__ == '__main__':
    print(part1())
