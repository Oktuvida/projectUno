class jugadas:
    def __init__ (self, cartaJugada:dict or str, barajaJugador:list, turn:int=1):
        if isinstance(cartaJugada, dict):
            self.cartaJugadaKey = list(cartaJugada.keys())[0]
            self.cartaJugadaValue = list(cartaJugada.values())[0]
        else:
            self.cartaJugadaKey = self.cartaJugadaValue = cartaJugada
        self.barajaJugadorKey=[]
        self.barajaJugadorValue=[]
        for elements in barajaJugador:
            if isinstance(elements, dict):
                self.barajaJugadorKey.append(list(elements.keys())[0])
                self.barajaJugadorValue.append(list(elements.values())[0])
            else:
                self.barajaJugadorKey.append(elements)
                self.barajaJugadorValue.append(elements)
        self.turn = turn

    def cartaJugadaInBarajaJugador(self):
        self.turn += 1
        if (not '+4' in self.cartaJugadaKey or not '+2' in self.cartaJugadaKey) and ((self.cartaJugadaKey in self.barajaJugadorKey or self.cartaJugadaKey in self.barajaJugadorValue) or (self.cartaJugadaValue in self.barajaJugadorValue if len(self.cartaJugadaValue)==1 else (self.cartaJugadaValue in self.barajaJugadorKey or self.cartaJugadaValue in self.barajaJugadorValue))):
            
            return True
        elif self.cartaJugadaKey == 'Change color' or ('+4' in self.cartaJugadaKey and ('and change color' in self.cartaJugadaValue or 'and change color' in self.barajaJugadorValue)):
            return True
        elif ('+2' in self.barajaJugadorKey or '+4' in self.barajaJugadorKey) and (self.cartaJugadaValue in self.barajaJugadorValue):
            return True
        else:
            return False

    def initialCardIsChangeColorOrPlus(self):
        if self.turn == 1:
            if self.cartaJugadaKey == 'Change color':
                return 1
            elif '+4' in self.cartaJugadaKey:
                return 2
            else:
                return 3

    def cartaJugadaNotInBarajaAndIsPlus(self):
        if not ('+4' in self.cartaJugadaKey or '+2' in self.cartaJugadaKey):
            return True
        elif '+4' in self.cartaJugadaKey:
            return int(4)
        else:
            return int(2)


    def cardsAreEquals(self, card:dict):
        cardKey = list(card.keys())[0]
        cardValue = list(card.values())[0]
        if not ('+4' in self.cartaJugadaKey or '+2' in self.cartaJugadaKey) and (self.cartaJugadaKey == cardKey or self.cartaJugadaKey == cardValue) or (self.cartaJugadaValue == cardValue if len(self.cartaJugadaValue)==1 else (self.cartaJugadaValue == cardKey or self.cartaJugadaValue == cardValue)):
            return True
        else:
            return False

    def cardIsChangeColor(self, card:dict or str):
        if card == 'Change color' and (not '+4' in card or not '+2' in card):
                return True
        else:
                return False

    def cardIsPlus4(self, card:dict or str):
        if '+4 and change color' in card:
            return True
        else:
            return False
            
