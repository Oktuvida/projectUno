from random import randint, choice

def colorCards():
    return ['Red', 'Blue', 'Green', 'Yellow']

def jokerCards():
    return ['+2', 'Change direction', 'Block', 'Change color', '+4 and change color']
    
class deckCards:
    def __init__(self):
        self.verify = True
        self.deckComplete = list()
        self.deckCompleteOP = list()
        for color in colorCards():
            for num in range(10):
                for numCards in range (2 if num!=0 else 1):
                    self.deckComplete.append({'./images/CARTAS PROYECTO/{0}{1}.png'.format(num,color[0]):{'{0}'.format(color):'{0}'.format(num)}})
                    self.deckCompleteOP.append('./images/cartasProyectoOP/{0}{1}.png'.format(num,color[0]))
            for joker in jokerCards():
                if not ('+4' in joker or 'Change c' in joker):
                    if '+2' in joker:
                        for numCard in range (2):
                            self.deckComplete.append({'./images/CARTAS PROYECTO/+2{0}.png'.format(color[0]) : {'{0}'.format(color):'{0}'.format(joker)}})
                            self.deckCompleteOP.append('./images/cartasProyectoOP/+2{0}.png'.format(color[0]))
                    elif 'Change d' in joker:
                        for numCard in range (2):
                            self.deckComplete.append({'./images/CARTAS PROYECTO/CD{0}.png'.format(color[0]) : {'{0}'.format(color): '{0}'.format(joker)}})
                            self.deckCompleteOP.append('./images/cartasProyectoOP/CD{0}.png'.format(color[0]))
                    else:
                        for numCard in range(2):
                            self.deckComplete.append({'./images/CARTAS PROYECTO/B{0}.png'.format(color[0]) : {'{0}'.format(color):'{0}'.format(joker)}})
                            self.deckCompleteOP.append('./images/cartasProyectoOP/B{0}.png'.format(color[0]))
        for numCard in range (4):
            self.deckComplete.append({'./images/CARTAS PROYECTO/CC.png' : 'Change color'})
            self.deckCompleteOP.append('./images/cartasProyectoOP/CC.png')
        for numCard in range (4):
            self.deckComplete.append({'./images/CARTAS PROYECTO/+4CC.png' : '+4 and change color'})
            self.deckCompleteOP.append('./images/cartasProyectoOP/+4CC.png')


    def selectCard(self):
        if len(self.deckComplete)>=1:
            randomIndex = randint(0, len(self.deckComplete)-1)
            cardChoiceOP = self.deckCompleteOP[randomIndex]
            cardChoice = self.deckComplete[randomIndex]
            self.deckComplete.pop(randomIndex)
            self.deckCompleteOP.pop(randomIndex)
            return cardChoice, cardChoiceOP
        return 'Ya no hay más cartas en la baraja'
    
    def addCard(self, deckPlayer:list, deckPlayerOP:list):
        if len(self.deckComplete)<1:
            return False
        else:
            cardChoice, cardChoiceOP = self.selectCard()
            deckPlayer.append(cardChoice)
            deckPlayerOP.append(cardChoiceOP)
            return deckPlayer, deckPlayerOP
            