_EXAMPLE = [[0,3,6,9,12,15], [1,3,6,10,15,21], [10,13,16,21,30,45]]

def read_file(filename: str) -> list: 
    with open(filename, 'r') as file:
        return file.readlines()
    
def parse_line(line: str) -> list:
    tmp = line.split(" ")
    return [int(value.strip()) for value in tmp]

def calculate_values(line: list) -> list: 
    values = []
    values.append(line)
    while sum(values[-1]) != 0:
        tmp = []
        for i, value in enumerate(values[-1]):
            if i + 1 < len(values[-1]):
                tmp.append(values[-1][i+1] - value)
        values.append(tmp)
    return values

def calculate_next(values: list) -> int: 
    sum = 0
    for value in values:
        sum += value[-1]
    return sum

def test():
    pyramids = []
    for list in _EXAMPLE:
        pyramids.append(calculate_values(list))
    sums = []
    for pyramid in pyramids:
        sums.append(calculate_next(pyramid))
    print(sums)
    print(sum(sums))

def main():
    lines = read_file("9th/input.txt")
    values = [parse_line(line) for line in lines]
    print(values)
    pyramids = [calculate_values(list) for list in values]
    print(pyramids)
    sums = [calculate_next(pyramid) for pyramid in pyramids]
    print(sums)
    print(sum(sums))

main()