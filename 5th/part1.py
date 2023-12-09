# testing
seeds = [79, 14, 55, 13]

"""
seed-to-soil map:
50 98 2
52 50 48
dest range start, source range start, range length
"""

def map_seed(seed: int, ranges: tuple):
    source = [i for i in range(ranges[1], ranges[1] + ranges[2])]
    dest = [i for i in range(ranges[0], ranges[0] + ranges[2])]
    try:
        return dest[source.index(seed)]
    except ValueError:
        return seed

def test():
    for seed in seeds:
        print(f"Seed: {seed} - dest: {map_seed(seed, (52, 50, 48))}")

test()