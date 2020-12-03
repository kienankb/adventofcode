import re

def part1():
    pattern = r"(\d+)-(\d+) (\w): (\w+)$"
    validCount = 0
    for line in open('01-input.txt', 'r'):
        m = re.match(pattern, line.strip())
        lowerBound = int(m.group(1))
        upperBound = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        count = password.count(char)
        if count >= lowerBound and count <= upperBound:
            validCount += 1
    return validCount

def part2():
    pattern = r"(\d+)-(\d+) (\w): (\w+)$"
    validCount = 0
    for line in open('01-input.txt', 'r'):
        m = re.match(pattern, line.strip())
        firstPos = int(m.group(1))
        secondPos = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        if (password[firstPos-1] == char or password[secondPos-1] == char) and password[firstPos-1] != password[secondPos-1]:
            validCount += 1
    return validCount

print(part1())
print(part2())
