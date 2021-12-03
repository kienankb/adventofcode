def part1():
    diagnostics = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for report_line in open('03-01-input.txt', 'r'):
        for i, bit in enumerate(report_line.strip()):
            if bit == '1':
                diagnostics[i] += 1
            elif bit == '0':
                diagnostics[i] -= 1
    gamma = [1 if x > 0 else 0 for x in diagnostics]
    epsilon = [0 if x > 0 else 1 for x in diagnostics]
    gamma_int = int(''.join(str(i) for i in gamma), 2)
    epsilon_int = int(''.join(str(i) for i in epsilon), 2)
    print(gamma_int * epsilon_int)

def part2():
    pass

part1()
part2()
