from string import digits

# Read lines from a given file-name and return them as a list
def read_file(name: str) -> list:
    with open(name, 'r') as file:
        return file.readlines()
    
# Combine first and last digit of a given line and return resulting str
# If only one digit present in a line will return a str consisting of two of those
def combine_integers(line: str) -> int:
    integers = [char for char in line if char in digits]
    if len (integers) == 1:
        return integers[0] * 2
    else:
        return integers[0] + integers[-1]
    
# return a 
def sum_str(integers: list) -> int:
    sum = 0
    for integer in integers:
        sum += int(integer)
    return sum

def main():
    lines = read_file("input.txt")
    integers = [combine_integers(line) for line in lines]
    sum = sum_str(integers)
    print (sum)

main()