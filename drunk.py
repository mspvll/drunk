from re import T


class Card:
    suits = ["пикей",
             "червей",
             "бубей",
             "треф"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "валета", "даму",
              "короля", "туз"]
    def __init__(self, v, s):
        """suits and values - целые числа"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        
        if self.value == c2.value:
            if self.suit < c2.suit:
               return True
            else:
                return False
        return False




    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        
        if self.value == c2.value:
            if self.suit > c2.suit:
               return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " " + self.suits[self.suit]
        return v
c1 = Card(10, 1)
c2 = Card(11, 2)
print(c1 < c2)
print (c1)



#колода


from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return "колода пуста"
        return self.cards.pop()

    
#d=Deck()
"""for card in d.cards:
    print(card)"""

"""print(d.cards)
print(" ")
print(d.rm_card())
print()
print(d.cards)"""


class Player:
    def __init__(self, n):
        self.name = n
        self.card = None
        self.wins = 0
        


class Game:
    def __init__(self):
        self.deck = Deck()
        name1 = input("введите имя игрока 1: ")
        name2 = input("введите имя игрока 2: ")
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
    def play_game(self):
        cards = self.deck.cards
        print("Игра началась!")
        while len(cards) >= 2:
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            print(f"{p1n} кладет {p1c}, а {p2n} кладет {p2c} .")
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(p1n)
            else:
                self.p2.wins +=1
                self.wins(p2n)

        print(f"У {self.p1.wins} побед, у {self.p2.wins} побед")
        if self.p1.wins > self.p2.wins:
            print(f"{p1n} выиграл! Игра окончена")
        elif self.p2.wins > self.p1.wins:
            print(f"{p2n} выиграл! Игра окончена")
        else:
            print(f"Ничья! Игра окончена")

    def wins(self,winner):
        print(f"{winner} забирает карты")

Game().play_game()
