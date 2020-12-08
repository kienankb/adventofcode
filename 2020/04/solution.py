def part1():
    neededFields= ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validPassports = 0
    passportDict = {}
    for line in open('./04-input.txt', 'r'):
        if line != "\n":
            lineFields = line.strip().split(' ')
            for field in lineFields:
                passportDict[field.split(':')[0]] = True
        else:
            if all([field in passportDict.keys() for field in neededFields]):
                validPassports += 1
            passportDict.clear()
    if all([field in passportDict.keys() for field in neededFields]):
        validPassports += 1
    return validPassports

def part2():
    pass

print(part1())
print(part2())
