races = (44899691, 277113618901768)
races2 = (71530, 940200)

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
    margin = calculate_margin(races)
    print(margin)
main()