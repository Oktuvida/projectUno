from deck import colorCards

def wordTaken(mazo:list=None):
    if not(mazo==None):
        while True:
            try:
                filaSeleccionada = int(input('\nSelecciona una fila: '))
                if filaSeleccionada > len(mazo) or filaSeleccionada <= 0:
                    print('\nError. Tal fila no está en tu baraja')
                    continue
            except ValueError:
                print('\nError. Digita un número')
            else:
                return filaSeleccionada
    else:
        while True:
            try:
                colorChange = str(input('Digita el color que deseas:')).lower()
                if not (colorChange in colorCards()):
                        print('\nError. {0} no es un color/palabra disponible.'.format(colorChange))
                        continue
            except ValueError:
                print('\nError. Digita una palabra')
            else:
                return colorChange