from deck import baraja
from player import jugador
from moves import jugadas
from inputReview import wordTaken
from os import system
from time import sleep

b1 = baraja()
p1 = jugador(b1)


mazoInicialP1 = p1.mazoInicial
initialCard = b1.selectCard()

system('clear')

endGame = False
while not endGame:
    print('La carta jugada es: {0}\n'.format(initialCard))
    print('Tu mazo es:')
    fila = 0
    for elements in mazoInicialP1:
        print('{0}. {1}'.format(fila+1, elements))
        fila+=1
    reviewOfPlay = jugadas(initialCard, mazoInicialP1)
    if reviewOfPlay.initialCardIsChangeColorOrPlus() == 1:
        initialCard = wordTaken()
        print('La carta jugada es: {0}\n'.format(initialCard))
    elif reviewOfPlay.initialCardIsChangeColorOrPlus() == 2:
        initialCard = {'+4':wordTaken()}
        print('La carta jugada es: {0}\n'.format(initialCard))
    if reviewOfPlay.cartaJugadaInBarajaJugador():
        filaSeleccionada = wordTaken(mazoInicialP1)
        cartaSeleccionada = mazoInicialP1[filaSeleccionada-1]
        if reviewOfPlay.cardIsChangeColor(cartaSeleccionada):
            initialCard = wordTaken()
            mazoInicialP1.remove(cartaSeleccionada)
        elif reviewOfPlay.cardIsPlus4(cartaSeleccionada):
            initialCard = {'+4': wordTaken()}
            mazoInicialP1.remove(cartaSeleccionada)
        elif reviewOfPlay.cardsAreEquals(cartaSeleccionada):
            mazoInicialP1.remove(cartaSeleccionada)
            initialCard = cartaSeleccionada
        else:
            print('La carta que elegiste no es compatible con la que está en juego.\n')
    else:
        if len(mazoInicialP1) <= 0:
            endGame=True
        elif reviewOfPlay.cartaJugadaNotInBarajaAndIsPlus()==False:
            print('La carta jugada no está en tu mazo, debes tomar carta\n')
            if b1.addCard(mazoInicialP1)==False:
                print('No hay más cartas en la baraja')
                endGame = True
            else:
                b1.addCard(mazoInicialP1)
                print('Se agregó la carta {0}'.format(mazoInicialP1[-1]))
                sleep(0.5)
        else:
            print('Debes tomar 4 cartas' if '+4' in initialCard else 'Debes tomar 2 cartas')
            for i in range (reviewOfPlay.cartaJugadaNotInBarajaAndIsPlus()):
                if b1.addCard(mazoInicialP1)==False:
                    print('No hay más cartas en la baraja')
                    endGame = True
                else:
                    b1.addCard(mazoInicialP1)
                    print('Se agregó la carta {0}'.format(mazoInicialP1[-1]))
                    sleep(0.5)
    sleep(0.5)