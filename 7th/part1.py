POINTS = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

class Hand:
    def __init__(self, cards: list) -> None:
        self.cards = cards
        self.value = 0
        self.__calculate_value()

    # 6. Five of a kind, where all five cards have the same label: AAAAA
    # 5. Four of a kind, where four cards have the same label AA8AA
    # 4. Full house, where three cards have the same label 23332
    # 3. Three of a kind, where three cards have the same label TTT98
    # 2. Two pair, where two cards share one label, 23432
    # 1. One pair, where two cards share one label, A23A4
    # 0. High card, where all cards' labels are distinct: 23456 
    def __calculate_value(self):
        tmp = self.cards[:]
        while len(tmp) > 0:
            card = tmp.pop()
            count = self.cards.count(card)
            if count > 1:
                if count == 5:
                    self.value = 6
                    return
                elif count == 4:
                    self.value = 5
                    return
                elif count == 3:
                    self.value += 3
                elif count == 2:
                    self.value += 1
                try:
                    while True:
                        tmp.remove(card)
                except ValueError:
                    continue

    def get_value(self):
        return self.value
    
    def __repr__(self) -> str:
        return f"{self.cards} and value {self.get_value()}"




def readfile(filename: str):
    with open(filename, 'r') as file:
        return file.readlines()
    
def test():
    decks = [['3','2','T','3','K'], ['T','5','5','J','5'],['K','K','6','7','7'],['K','T','J','J','T'],['Q','Q','Q','J','A']]
    hands = [Hand(deck) for deck in decks]
    for hand in hands:
        print(hand)
    
test()