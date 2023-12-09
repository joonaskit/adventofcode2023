from input import races_part1

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
    margins = [calculate_margin(race) for race in races_part1]
    print(f"{margins}")
    multiplication = 1
    for margin in margins:
        multiplication = margin * multiplication
    print(f"Multiplication = {multiplication}")

main()