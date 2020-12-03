def parseInput():
    return [int(expense) for expense in open('./01-input.txt', 'r')]

def part1():
    expenses = parseInput()
    while len(expenses) > 0:
        targetExpense = expenses.pop()
        for expense in expenses:
            if expense + targetExpense == 2020:
                return targetExpense * expense

def part2():
    expenses = parseInput()
    for i in expenses:
        for j in expenses:
            for k in expenses:
                if i != j and i != k and i + j + k == 2020:
                    return i * j * k

print(part1())
print(part2())
