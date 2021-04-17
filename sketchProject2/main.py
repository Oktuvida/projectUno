from jugador import jugador
from baraja import baraja

b1 = baraja()
""" for i in range(5):
    initialCard = b1.addCard()
    print(initialCard)
print('red = {0}\nyellow {1}'.format(b1.baraja['red'], b1.baraja['yellow'])) """
for i in range(50):
    initialCard = b1.addCard()
    print (initialCard)