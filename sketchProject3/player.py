from deck import baraja

class jugador:
    def __init__ (self, baraja):
        self.mazoInicial = [baraja.selectCard() for x in range(7)]
        
    def __str__(self):
        return '{0}'.format(self.mazoInicial)