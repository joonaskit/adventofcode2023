from string import digits

INT_DICT = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def read(name: str) -> list:
    with open(name, 'r') as file:
        return file.readlines()

def get_index(pair: tuple) -> int:
    return pair[0]

def find_all(line, substring):
    start = 0
    while True:
        start = line.find(substring, start)
        if start == -1: return
        yield start
        start += len(substring)

def parse_line(line: str) -> list:
    parts = []
    for key, value in INT_DICT.items():
        if key in line:
            tmp = list(find_all(line, key))
            for tmp_value in tmp:
                parts.append((tmp_value, value))
    for i, char in enumerate(line):
        if char in digits:
            parts.append((i, char))
    parts.sort(key=get_index)
    return parts


def sum(lines: list) -> int:
    ints = []
    sum = 0
    for line in lines:  
        ints.append(parse_line(line))
    for number in ints:
        if len(number) == 1:
            sum += int(number[0][1] + number[0][1])
        else:
            sum += int(number[0][1] + number[-1][1])
    return sum

def main():
    lines = read("first/input.txt")
    print(sum(lines))

main()