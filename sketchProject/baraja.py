from random import randint

def lessColor(self, originalDicty:dict, lessKey:str='color'):
        del originalDicty[lessKey]
        return originalDicty
class baraja:
    def __init__ (self, red:int=25, green:int=25, blue:int=25, \
        yellow:int=25, joker:int=8, customizable:int=3, \
        specialRule:int=1):
        self.baraja=[{'red':red, 'green':green, 'blue':blue, \
        'yellow':yellow,},{
        'joker':joker,
        'customizable':customizable,
        'specialRule':specialRule
        }]

    def initialCard(self):
        colors = list(self.baraja[0].keys())
        initialCard = {colors[randint(0, 3)]:randint(1, 9)}
        return initialCard
        
    