from deck import deckCards

class jugador:
    def __init__(self, deck):
        self.mazo = [deck.selectCard() for x in range (7)]