from deck import deckCards

class jugador:
    def __init__(self, deck):
        self.mazo = list()
        self.mazoOP = list()
        for x in range(1):
            card, cardOP = deck.selectCard()
            self.mazo.append(card)
            self.mazoOP.append(cardOP)