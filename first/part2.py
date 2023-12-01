from string import digits

def read(name: str) -> list:
    with open(name, 'r') as file:
        return file.readlines()

def get_index(pair: tuple) -> int:
    return pair[0]

def find_first_last(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def sum(lines: list) -> int:
    int_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    ints = []
    sum = 0
    for line in lines:
        parts = []
        for key, value in int_dict.items():
            i = line.find(key)
            if i >= 0:
                tmp = list(find_first_last(line, key))
                if len(tmp) == 1:
                    parts.append((tmp[0], value))
                else:
                    parts.append((tmp[0], value))
                    parts.append((tmp[-1], value))
        for i, char in enumerate(line):
            if char in digits:
                parts.append((i, char))
        parts.sort(key=get_index)
        ints.append(parts)
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