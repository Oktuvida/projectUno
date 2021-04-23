from random import choice

def colorCardValues():
    #Crea un diccionario con los valores del color de una carta y la respectiva cantidad que hay de ellas
    valueList = ['0']
    valueList.extend('{0}'.format(x+1) for x in range(9))
    return dict.fromkeys(valueList, 2)

def jokerCardValues():
    #Crea un diccionario con la cantidad de comodines que hay por color de carta
    colorCardsList = ['red', 'blue', 'green', 'yellow']
    return dict.fromkeys(colorCardsList, 2)

def restValue(dictionary:dict, allDicty:bool=True, key1:str='0'):
    #Es una función exclusiva para acomodar el valor '0' de las cartas con color a 1.
    if allDicty:
        for key0 in dictionary:
            dictionary[key0][key1] -= 1
    else:
        dictionary[key1] -= 1
    return dictionary

def colorCards():
    return ['red', 'blue', 'green', 'yellow']

class baraja:
    def __init__(self):
        self.verify=True
        self.cardColors = {'red':colorCardValues(), 'blue':colorCardValues(), 'green':colorCardValues(), 'yellow':colorCardValues()}
        restValue(self.cardColors)
        
        self.jokerCards = {'+2':jokerCardValues(), 'Change direction':jokerCardValues(), 'Block':jokerCardValues(), 'Change color':4, '+4 and change color':4}

        self.deckComplete = self.cardColors.copy()
        self.deckComplete.update(self.jokerCards)
    
    def __str__(self):
        return '{0}'.format(self.deckComplete)

    def selectCard(self):
        if self.verify:
            keyList = list(self.deckComplete.keys())
            if len(keyList) >= 1:
                randomKey = choice(keyList)
            while len(self.deckComplete)>=1:
                if 'Change color' in randomKey or '+4 and change color' in randomKey:
                    if self.deckComplete[randomKey]>=1:
                        self.deckComplete[randomKey] -= 1
                        self.jokerCards[randomKey] -= 1
                        return '{0}'.format(randomKey)
                    else:
                        del self.deckComplete[randomKey]
                else:
                    keyList1 = list(self.deckComplete[randomKey].keys())
                    if len(keyList1) >= 1:
                        randomKey1 = choice(keyList1)
                        if self.deckComplete[randomKey][randomKey1]>= 1:
                            self.deckComplete[randomKey][randomKey1] -= 1
                            return {'{0}'.format(randomKey): randomKey1}
                        else:
                            del self.deckComplete[randomKey][randomKey1]
                    else:
                        del self.deckComplete[randomKey]
                keyList = list(self.deckComplete.keys())
                if len(keyList) >= 1:
                    randomKey = choice(keyList)
        self.verify=False
        return 'Ya no hay más cartas en el mazo'

    def addCard(self, deckPlayer:list):
        if not self.verify:
            return False
        else:
            deckPlayer.append(self.selectCard())