# The Elf would first like to know which games would have been possible if the bag 
# contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

from string import digits

_MAX_COLORS = {'green':13, 'blue':14, 'red':12}

def read_file(filename: str) -> list:
    with open(filename, 'r') as file:
        return file.readlines()

def parse_round(round: str, values: dict):
    if ',' in round:
        colors = round.split(',')
        for color in colors:
            tmp = color.strip().split(" ")
            if tmp[1].strip() in values:
                if values[tmp[1].strip()] < int(tmp[0].strip()):
                    values[tmp[1].strip()] = int(tmp[0].strip())
            else:
                values[tmp[1].strip()] = int(tmp[0].strip())
    else:
        tmp = round.strip().split(" ")
        if tmp[1].strip() in values:
            if values[tmp[1].strip()] < int(tmp[0].strip()):
                values[tmp[1].strip()] = int(tmp[0].strip())
            else:
                values[tmp[1].strip()] = int(tmp[0].strip())

    
def parse_colors(game: str) -> dict:
    rounds = game.split(';')
    color_values = {}
    for round in rounds:
        parse_round(round, color_values)
    return color_values

    
def parse_game(line: str) -> list:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 15 green, 20 red, 8 blue; 12 green, 7 red; 10 green, 2 blue, 15 red; 13 blue, 15 red
    game = line.split(':')
    colors = parse_colors(game[1])
    game[1] = colors
    game[0] = int(game[0].split(" ")[1].strip())
    return game

def possible(game: dict) -> bool:
    for key, value in game.items():
        if _MAX_COLORS[key] < value:
            return False
    return True

def print_games(games: list) -> None:
    for game in games:
        if possible(game[1]):
            print(f"Game: {game[0]}: {game[1]} TRUE")
        else:
            print(f"Game: {game[0]}: {game[1]} FALSE")

def main():
    lines = read_file("2nd/input2.txt")
    games = [parse_game(line) for line in lines]
    print_games(games)
    sum = 0
    for game in games:
        if possible(game[1]):
            sum += game[0]
    print(sum)

main()