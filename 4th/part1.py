class Card:
    def __init__(self, details: list) -> None:
        self.__winning = details[1]
        self.__numbers = details[2]
        self.__id = details[0]
        self.__clean(self.__winning)
        self.__clean(self.__numbers)

    def __clean(self, numbers: list) -> None:
        while '' in numbers:
            numbers.remove('')
    
    def __count_winning(self) -> int:
        sum = 0
        for number in self.__numbers:
            if number in self.__winning:
                sum += 1
        return sum
    
    def count_points(self) -> int:
        sum = self.__count_winning()
        if sum > 1: 
            points = 1
            return pow((points * 2), (sum - 1))
        elif sum == 1:
            return 1
        else:
            return 0
    
    def __str__(self) -> str:
        return f"Card {self.__id}: {self.__winning} | {self.__numbers}"
        
def read_file(filename: str)-> list:
    with open(filename, 'r') as file:
        return file.readlines()
    
def parse_line(line: str) -> list:
    card = line.strip().split(':')
    id = int(card[0].strip().split(' ')[-1].strip())
    numbers = card[1].strip().split('|')
    return  [id, numbers[0].strip().split(" "), numbers[1].strip().split(" ")]

def main():
    lines = read_file("4th/input.txt")
    cards = []
    sum = 0
    for line in lines:
        cards.append(Card(parse_line(line)))
    for card in cards:
        print(card)
        points = card.count_points()
        print(f"Points: {points}")
        sum += points
    print (f"Sum: {sum}")

main()
        