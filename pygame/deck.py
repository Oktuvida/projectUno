from random import randint, choice

def colorCards():
    return ['Red', 'Blue', 'Green', 'Yellow']

def jokerCards():
    return ['+2', 'Change direction', 'Block', 'Change color', '+4 and change color']
    
class deckCards:
    def __init__(self):
        self.verify = True
        self.deckComplete = []
        for color in colorCards():
            for num in range(10):
                for numCards in range (2 if num!=0 else 1):
                    self.deckComplete.append({'./images/CARTAS PROYECTO/{0}{1}.png'.format(num,color[0]):{'{0}'.format(color):'{0}'.format(num)}})
            for joker in jokerCards():
                if not ('+4' in joker or 'Change c' in joker):
                    if '+2' in joker:
                        for numCard in range (2):
                            self.deckComplete.append({'./images/CARTAS PROYECTO/+2{0}.png'.format(color[0]) : {'{0}'.format(color):'{0}'.format(joker)}})
                    elif 'Change d' in joker:
                        for numCard in range (2):
                            self.deckComplete.append({'./images/CARTAS PROYECTO/CD{0}.png'.format(color[0]) : {'{0}'.format(color): '{0}'.format(joker)}})
                    else:
                        for numCard in range(2):
                            self.deckComplete.append({'./images/CARTAS PROYECTO/B{0}.png'.format(color[0]) : {'{0}'.format(color):'{0}'.format(joker)}})
        for numCard in range (4):
            self.deckComplete.append({'./images/CARTAS PROYECTO/CC.png' : 'Change color'})
        for numCard in range (4):
            self.deckComplete.append({'./images/CARTAS PROYECTO/+4CC.png' : '+4 and change color'})

    def selectCard(self):
        if len(self.deckComplete)>=1:
            randomIndex = randint(0, len(self.deckComplete)-1)
            cardChoice = self.deckComplete[randomIndex]
            self.deckComplete.pop(randomIndex)
            return cardChoice
        return 'Ya no hay más cartas en la baraja'
    
    def addCard(self, deckPlayer:list):
        if len(self.deckComplete)<1:
            return False
        else:
            return deckPlayer.append(self.selectCard())
            