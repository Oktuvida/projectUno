from random import randint

class baraja:
    #Se inicializa la baraja con parámetros estándares.
    def __init__(self):
        colorCards = {'{0}'.format(x+1):2 for x in range(9)}
        colorCards['0']=1
        self.baraja = {'red': colorCards, 'blue': colorCards, 'green': colorCards, 'yellow': colorCards, 'joker': 8}
        self.barajaCopy = self.baraja
        self.jokerValues=['enter a color', 2, 4, 'direction change', 'cart useless']

    #Retorna el estado de la baraja
    def __str__ (self):
        return '{0}'.format(self.baraja)

    #Se escoge una carta al azar, útil tanto para iniciar el juego como para 'comer' cartas
    def addCard(self):
        initialColorCards = list(self.barajaCopy.keys())[:4]
        indexDefault = 4
        while len(self.baraja)>0:
            #Se hace una lista con todas las palabras clave del diccionario 'baraja'.
            cards = list(self.baraja.keys())
            #Se escoge un índice al azar.
            indexSelected = randint(0, len(cards)-1)
        
            if indexSelected in range(0, indexDefault) and cards[indexSelected] in initialColorCards:
                if len(self.baraja[cards[indexSelected]]) >= 1:
                        colorValuesKey = list(self.baraja[cards[indexSelected]].keys())
                        indexRandom = randint(0, len(colorValuesKey)-1)
                        randomKey = colorValuesKey[indexRandom]
                        if self.baraja[cards[indexSelected]][randomKey] >= 1:
                            self.baraja[cards[indexSelected]][randomKey] -=1
                            colorItem = list(self.baraja[cards[indexSelected]].items())[indexRandom][0]
                            cardSelected = {cards[indexSelected]: {colorItem:self.baraja[cards[indexSelected]][randomKey]}}
                            return cardSelected
                        else:
                            del self.baraja[cards[indexSelected]][randomKey]
                else:
                    del self.baraja[cards[indexSelected]]
                    indexDefault -= 1
            elif self.baraja['joker'] >= 1:
                    self.baraja[cards[indexSelected]] -= 1
                    cardSelected = {cards[indexSelected]: self.baraja[cards[indexSelected]]}
                    return cardSelected
            else:
                del self.baraja[cards[indexSelected]]
        return None
        #Si son colores, retornará un valor entre 1 a 9, si es un joker, se pedirá al usuario que digite un color, si es un customizable, se retornará 2 o 4.
"""         cardSelected = {cards[indexSelected]: randint(0, 9) if indexSelected in range(0, 3) else self.jokerValues[randint(0, len(self.jokerValues)-1)] """
        
        #Se descontará de la baraja la carta inicial.
"""         keyCardSelected = list(cardSelected.keys())[0]
        if keyCardSelected in self.baraja[:3]:
            self.baraja[keyCardSelected] =  """