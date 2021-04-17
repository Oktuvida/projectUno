from baraja import baraja
from jugador import jugador, addCards
from random import randint
from os import system

p1 = jugador()
p2 = jugador()

cardsP1 = p1.cartas()
b1 = baraja()

initialCard = b1.initialCard()
initialNumber = list(initialCard.values())[0]
initialColor = list(initialCard.keys())[0]
deck = b1.baraja[0]
deck[initialColor] -= 1


b1Copy = b1.baraja[0]
del b1Copy[initialColor]
colorKey1 = list(b1Copy.keys())[0]
del b1Copy[colorKey1]
colorKey2 = list(b1Copy.keys())[0]
del b1Copy[colorKey2]
colorKey3 = list(b1Copy.keys())[0]

for i in cardsP1:
    x = list(i.keys())[0]
    deck[x] -= 1


cardPlayed = initialCard

print(deck)


while len(cardsP1)>=1:
    system('clear')
    colorCardPlayed = list(cardPlayed.keys())[0]
    numberCardPlayed = list(cardPlayed.values())[0]
    print('\nCard played: {0}'.format(cardPlayed))
    counter = 1
    print('\nYour cards are: ')
    for cards in cardsP1:
        print('{0}. {1}'.format(counter, cards))
        counter+=1
    cartaJugada = int(input('\nWrite the number of the row you want: '))
    while cartaJugada > len(cardsP1) or cartaJugada<=0:
        cartaJugada = int(input('Error, try again: '))
    selection = cardsP1[cartaJugada-1]
    colorSelection = list(selection.keys())[0]
    numberSelection = list(selection.values())[0]
    if colorSelection == colorCardPlayed or numberSelection == numberCardPlayed:
        cardPlayed = selection
        del cardsP1[cartaJugada-1]
    else:
        addCards(cardsP1)
print('You\'ve won!')