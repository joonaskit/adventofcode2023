races = [(44, 277), (89, 1136), (96, 1890), (91, 1768)]
races2 = [(7, 9), (15, 40), (30, 200)]

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
    margins = [calculate_margin(race) for race in races]
    print(f"{margins}")
    multiplication = 1
    for margin in margins:
        multiplication = margin * multiplication
    print(f"Multiplication = {multiplication}")

main()