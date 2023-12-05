class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        fullRank = 'a' # how to get full name of rank?
        fullSuit = 'b'
        return '{} of {}'.format(fullRank, fullSuit)

    def value(self):
        return 10

class Deck:
    def __init__(self):
        # Create a list of 52 card objects
        self.deck = []
        for suit in ['c', 'd', 'h', 's']:
            for rank in range(1, 14):
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        pass

    def draw(self, num):
        pass
