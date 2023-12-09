from input import races_part2

# (time, distance) | (ms, mm)
# s = vt

def calculate_distance(v: int, t: int):
    return v*t

def calculate_margin(pair: tuple) -> int:
    margin = 0
    for i in range (pair[0]):
        t = pair[0] - i
        v = i
        if calculate_distance(v, t) > pair[1]:
            margin += 1
    return margin

def main():
    margin = calculate_margin(races_part2)
    print(margin)
main()