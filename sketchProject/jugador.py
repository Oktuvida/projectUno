from random import randint

def colors():
        colors = ['red', 'green', 'blue', 'yellow']
        return colors
def addCards(aList:list):
    color = colors()
    return aList.append({color[randint(0, 3)]:randint(1, 9)})
class jugador:
    def __init__ (self, cartas:int=7):
        color = colors()
        self.cards = [{color[randint(0,3)]:randint(1, 9)} for x in range (cartas)]
    def cartas(self):
        return self.cards
        