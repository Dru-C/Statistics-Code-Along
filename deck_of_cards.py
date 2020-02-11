import random

class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
    def show(self):
        print(f'{self.val} of {self.suit}')

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        suits = ['Spades','Clubs','Diamonds','Hearts']
        vals = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        for v in vals:
            for s in suits:
                self.cards.append(Card(v,s))
        random.shuffle(self.cards)
    def show(self):
        for c in self.cards:
            c.show()
    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self   
    def showHand(self):
        for card in self.hand:
            card.show()


deck = Deck()
deck.show()

bob = Player('Bob')

bob.draw(deck)
bob.showHand()

