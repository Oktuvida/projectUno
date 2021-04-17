from deck import baraja
from player import jugador
from moves import jugadas
from inputReview import wordTaken
from os import system

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
        changeColor = wordTaken(2)
        initialCard = changeColor
        print('La carta jugada es: {0}\n'.format(initialCard))
    elif reviewOfPlay.initialCardIsChangeColorOrPlus() == 2:
        changeColor = wordTaken(2)
        initialCard = {'+4':changeColor}
        print('La carta jugada es: {0}\n'.format(initialCard))
    if reviewOfPlay.cartaJugadaInBarajaJugador():
        filaSeleccionada = wordTaken(1, mazoInicialP1)
        cartaSeleccionada = mazoInicialP1[filaSeleccionada-1]
        if reviewOfPlay.cardIsChangeColor(cartaSeleccionada):
            colorChange = wordTaken(2)
            initialCard = colorChange
            mazoInicialP1.remove(cartaSeleccionada)
        elif reviewOfPlay.cardIsPlus4(cartaSeleccionada):
            colorChange = wordTaken(2)
            initialCard = {'+4': colorChange}
            mazoInicialP1.remove(cartaSeleccionada)
        elif reviewOfPlay.cardsAreEquals(cartaSeleccionada):
            mazoInicialP1.remove(cartaSeleccionada)
            initialCard = cartaSeleccionada
        else:
            print('La carta que elegiste no es compatible con la que está en juego.\n')
    else:
        if reviewOfPlay.cartaJugadaNotInBarajaAndIsPlus:
            print('La carta jugada no está en tu mazo, debes tomar carta\n')
            if b1.addCard(mazoInicialP1)==False:
                print('No hay más cartas en la baraja')
                endGame = True
            else:
                b1.addCard(mazoInicialP1)
        else:
            print('Debes tomar 4 cartas' if '+4' in initialCard else 'Debes tomar 2 cartas')
            for i in range (reviewOfPlay.cartaJugadaNotInBarajaAndIsPlus):
                if not b1.addCard(mazoInicialP1):
                    print('No hay más cartas en la baraja')
                    endGame = True
                else:
                    b1.addCard(mazoInicialP1)
            