from string import digits

all_numbers = []


def read_file(filename: str)-> list:
    with open(filename, 'r') as file:
        tmp = file.readlines()
        return [line.strip() for line in tmp]
    
def search_symbol(lines: list, line: str, i: int):
    for j, char in enumerate(line):
        # print(f"Char in index [{j}] is {char}")
        if char not in digits and char != '.':
            print(f"Searching for symbol {char} in line {i} and index {j}")
            search_cube(lines, i, j)

def search_cube(lines: list, i: int, j: int):
    if i > 0 and (i+1) < len(lines):
        for x in lines[i-1:i+2]:
            if j > 0 and (j+1) < len(x):
                for y in x[j-1:j+2]:
                    print(f"{y}", end="")
            print()

def add_number(line: str, start: int):
    tmp = []
    i = start
    while i < len(line) and line[i] in digits:
        tmp.append(line[i])
        i += 1
    return tmp, i


def gather_numbers(y: int, line: str):
    j = 0
    while j < len(line):
        if line[j] in digits:
            number, next = add_number(line, start=j)
            all_numbers.append(((y,j),number))
            print(f"Line {y} has number: {number} starting from index {j}")
            j = next
        else:
            j += 1

def part_ok(number: list, lines: list) -> bool:
    # check left
    if number[0][1] > 0:
        if lines[number[0][0]][(number[0][1] - 1)] != '.' and lines[number[0][0]][(number[0][1] - 1)] not in digits:
            return True
    
    # check right
    if (number[0][1] + len(number[1]) + 1) < len(lines[number[0][0]]):
        if lines[number[0][0]][number[0][1] + len(number[1])] != '.' and lines[number[0][0]][number[0][1] + len(number[1])] not in digits:
            return True
        
    # check above
    if number[0][0] > 0:
        for i in range(number[0][1],len(number[1]) + number[0][1]):
            if(lines[number[0][0] - 1][i] != '.' and lines[number[0][0] - 1][i] not in digits):
                return True
        # diagonally right
        if (number[0][1] + len(number[1])) < len(lines[0]):
            if lines[number[0][0] - 1][number[0][1] + len(number[1])] != '.' and lines[number[0][0] - 1][number[0][1] + len(number[1])] not in digits:
                return True
        # diagonally left
        if number[0][1] > 0:
            if lines[number[0][0] - 1][(number[0][1] - 1)] != '.' and lines[number[0][0] - 1][(number[0][1] - 1)] not in digits:
                return True

    # check below
    if number[0][0] + 1 < len(lines):
        for i in range(number[0][1],len(number[1]) + number[0][1]):
            if(lines[number[0][0] + 1][i] != '.' and lines[number[0][0] + 1][i] not in digits):
                return True
        # diagonally right
        if (number[0][1] + len(number[1])) < len(lines[0]):
            if lines[number[0][0] + 1][number[0][1] + len(number[1])] != '.' and lines[number[0][0] + 1][number[0][1] + len(number[1])] not in digits:
                return True
        # diagonally left
        if number[0][1] > 0:
            if lines[number[0][0] + 1][(number[0][1] - 1)] != '.' and lines[number[0][0] + 1][(number[0][1] - 1)] not in digits:
                return True
    
    return False

def check_engine_parts(lines: list):
    parts = []
    for number in all_numbers:
        if part_ok(number, lines):
            parts.append(number[1])
    return parts

def parse_values(parts: list):
    values = []
    for part in parts:
        tmp = ""
        for value in part:
            tmp += value
        values.append(tmp)
    return values

def sum_values(values):
    sum = 0
    for value in values:
        sum += int(value)
    return sum


def main():
    lines = read_file('3rd/input.txt')
    for y, line in enumerate(lines):
        gather_numbers(y, line)
    parts = check_engine_parts(lines)
    values = parse_values(parts)
    print(values)
    print(sum_values(values))

main()