import input

"""
seed-to-soil map:
50 98 2
52 50 48
dest range start, source range start, range length
"""

def read_file(filename: str) -> list:
    with open(filename, 'r') as file:
        return file.readlines()

def map_list(seed: int, map: list) -> int: 
    found = False
    for seed_range in map: 
        found, location = map_seed(seed, seed_range)
        if found:
            break
    return location

def map_seed(seed: int, ranges: tuple):
    if seed < ranges[1] or seed > ranges[1] + ranges[2]:
        return False, seed
    else: 
        i = seed - ranges[1]
        return True, ranges[0] + i

def main():
    locations = []
    for seed in input.seeds:
        tmp = map_list(seed, input.seed_to_soil)
        tmp = map_list(tmp, input.soil_to_fertilizer)
        tmp = map_list(tmp, input.fertilizer_to_water)
        tmp = map_list(tmp, input.water_to_light)
        tmp = map_list(tmp, input.light_to_temperature)
        tmp = map_list(tmp, input.temperature_to_humidity)
        locations.append((map_list(tmp,input.humidity_to_location), seed))
    lowest = min(locations, key=lambda location: location[0])
    print(lowest)
    
main()