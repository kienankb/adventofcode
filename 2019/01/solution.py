import math

def getFuelForMass(mass):
    fuel = math.floor(int(mass)/3)-2
    return fuel if fuel > 0 else 0

def part1():
    totalFuel = 0
    for moduleMass in open('01-input.txt'):
        totalFuel += getFuelForMass(moduleMass)
    return totalFuel

def part2():
    totalFuel = 0
    for moduleMass in open('01-input.txt'):
        fuel = getFuelForMass(moduleMass)
        while fuel > 0:
            totalFuel += fuel
            fuel = getFuelForMass(fuel)
    return totalFuel

if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
