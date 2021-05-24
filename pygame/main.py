
import pygame as pg 
from deck import deckCards
from player import jugador
from time import sleep
from moves import isEqual, findEqualCard, changeColor, isPlusFour, blockCard, reverseCard
from selectColor import selColor
from mouse import Cursor
from movies import isVideo
from buttoms import Boton

# Función que refresca la pantalla. Necesaria para la visualización en pygame.
def refreshScreen(frames, fps):
    pg.display.flip()
    frames.tick(fps)

# Función que muestra en pantalla la baraja del jugador.
def refreshDeck(mazoPlayerList, actualPlayer, mazoOPPlayerList, screenSize, width, height,
    initIndex, screen, cursor, rightArrowButtom, leftArrowButtom, dealCardsCounter,
    validDeal, dealCard, cardPlayed, frameCardOP, frameCard, frames, fps, nextPlay):
    # "actualPlayer" está limitado por la cantidad de usuarios, por lo cual, se debe verificar que no esté fuera de 
    # rango.
    if actualPlayer > len(mazoPlayerList)-1:
        actualPlayer = 0
    elif actualPlayer < 0:
        actualPlayer = len(mazoPlayerList)-1
    # Se actualiza el cursor.
    cursor.update()
    # La posición en x y y que tendrá cada imagen.
    xPos = screenSize[0]//5-width
    yPos = screenSize[0]//2+height//6
    # Inicialización de una lista que contedrá en ella múltiples clases Boton con parámetros pertenecientes a la baraja 
    # del jugador.
    deckPlayer = []
    for element1, element2 in zip(mazoPlayerList[actualPlayer], mazoOPPlayerList[actualPlayer]):            
        deckPlayer.append(Boton(element2,list(element1.keys())[0], xPos, yPos, width//2, height//2))
        xPos += width
    # Se limita la cantidad de imágenes visibles en pantalla a 7. Si es mayor a esta, aparecerán dos sprites encargados 
    # de recorrer la lista "deckPlayer".
    if len(deckPlayer)>7:
        if initIndex+7<len(deckPlayer):
            rightArrowButtom.update(screen, cursor)
            if cursor.colliderect(rightArrowButtom.rect) and pg.mouse.get_pressed()[0]:
                initIndex+=1
                nextPlay = True
                sleep(0.1)
        if initIndex-1 >= 0:
            leftArrowButtom.update(screen, cursor)
            if cursor.colliderect(leftArrowButtom.rect) and pg.mouse.get_pressed()[0]:
                initIndex-=1
                nextPlay = True
                sleep(0.1)
    # Se vuelve a inicialización la posición en x y y
    xPos = screenSize[0]//5-width
    yPos = screenSize[0]//2+height//6
    # Se inicializa una lista que contendrá la visualización de cada clase Boton anteriormente inicializada.
    imgDeckPlayer = []
    for element in deckPlayer[initIndex:initIndex+7]:
        # La primera vez que se visualiza la baraja de un jugador se mostrará carta por carta. Esta función se encarga 
        # de ello
        if dealCardsCounter < 2 and validDeal:
            try:
                if not ("change color" in list(cardPlayed.values())[0].lower()):
                    dealCard.play()
                else:
                    dealCardsCounter -= 1
            except:
                dealCard.play()
        # Si son cartas válidas con la que está en juego, el jugador recibirá una pequeña ayuda; se generará un marco 
        # muy minucioso alrededor de la carta válida.
        if isEqual(mazoPlayerList[actualPlayer][deckPlayer.index(element)], cardPlayed):
            frameCardButtom = Boton(frameCardOP, frameCard, xPos, yPos, width//2, height//2)
            frameCardButtom.update(screen, cursor)
        element.updatePosition(xPos, yPos)
        imgDeckPlayer.append(element)
        element.update(screen, cursor)
        xPos += width
        if dealCardsCounter < 2 and validDeal:
            try: 
                if not ("change color" in list(cardPlayed.values())[0].lower()):
                    refreshScreen(frames, fps)
                    sleep(0.4)
                else:
                    dealCardsCounter -= 1
            except:
                refreshScreen(frames, fps)
                sleep(0.4)
    if dealCardsCounter < 2 and validDeal:
        sleep(0.3)
    # Retorna valores que se requieren para que el código sucesor pueda ejecutarse. Entre ellas destaca imgDeckPlayer, 
    # el cual es una lista que contiene las cartas que están en pantalla.
    return nextPlay, initIndex, imgDeckPlayer, dealCardsCounter, actualPlayer


def minimizeWindow():
    pg.display.set_mode((1, 1))

def restoreWindow(screenSize):
    pg.display.set_mode(screenSize)


def game ():

    #Posición de ventana
    pg.init()
    
    #Fotogramas
    frames = pg.time.Clock()
    fps = 60

    #Conf pantalla
    screenSize = (960, 640)
    screen = pg.display.set_mode(screenSize)

    # Img fondo
    tablero = pg.transform.scale(pg.image.load("./esthetic/Tablero.png"), screenSize)

    #rect
    width = 125
    height = 190
    posX = (screenSize[0]//2)-width//2
    posY = screenSize[1]//3 - height//2
    

    #Baraja de cartas
    deckCard = deckCards()



    #Jugadores
    player1 = jugador(deckCard)
    mazoP1 = player1.mazo
    mazoP1OP = player1.mazoOP
    
    player2 = jugador(deckCard)
    mazoP2 = player2.mazo
    mazoP2OP = player2.mazoOP

    #playerList = [player1, player2]
    mazoPlayerList = [mazoP1, mazoP2]
    mazoOPPlayerList = [mazoP1OP, mazoP2OP]

    # Player active
    actualPlayer = 0

    #Arrows to watch deck
    initIndex = 0
    rightArrow = "./esthetic/Fde.png"
    rightArrowOp ="./esthetic/Fdeop.png"

    rightArrowButtom = Boton(rightArrow, rightArrowOp, screenSize[0]-55, screenSize[1]-100, 50, 50)
    leftArrowButtom = Boton(rightArrow, rightArrowOp, 5, screenSize[1]-100, 50, 50, True)

    #Mouse
    cursor = Cursor()

    #cardTaken
    cardTaken ="./esthetic/Cartare.png"
    cardTakenOP = "./esthetic/CartareOP.png"
    cardTakenButtom = Boton(cardTakenOP, cardTaken, 50, 40, width, height)

    # Marco alrededor de las cartas
    frameCard = "./esthetic/decoCard.png"
    frameCardOP = "./esthetic/decoCardOP.png"
    

    #PlayersImg
    imgPlayer1 = pg.image.load("./esthetic/player1.png")
    imgPlayer2 = pg.image.load("./esthetic/player2.png")
    
    # Contador de cartas tomadas y a tomar.
    cardTakenCounter = 0
    cardsTaken = 0
    noCardCounter = 0
    allCardsTaken = True

    # Uno Buttom
    unoPath = "./esthetic/Uno.png"
    unoOPPath = "./esthetic/Unop.png"
    unoButtom = Boton(unoPath, unoOPPath, 55, 325, 100, 100)
    buttomPressed = [False, False]

    #Carta jugada
    cardPlayed, cardPlayedOP = deckCard.selectCard()

    #Counter Block card
    blockCounter = 0
    isBlockCard = False
    
    #Reverse Block card
    playDirection = 1
    reverseCounter = 0
    isReverseCard = False

    # Fin del juego.
    gameOver = False

    # Music
    ambientSound = pg.mixer.music
    ambientSound.load("./music/ambient.mp3")
    ambientSound.set_volume(0.05)
    ambientSound.play()

    shuffleSound = pg.mixer.Sound("./music/barajar.wav")
    dealCard = pg.mixer.Sound("./music/repartir.wav")
    shuffleSound.play()

    # Dos variables únicamente para mostrar por primera vez la baraja del jugador.
    dealCardsCounter = 0
    validDeal = True

    while not gameOver:
        # Verifica que la variable que analiza el jugador actual no esté afuera de rango.
        if actualPlayer > len(mazoPlayerList)-1:
            actualPlayer = 0
        elif actualPlayer < 0:
            actualPlayer = len(mazoPlayerList)-1

        #Carta jugada
        figurePlayed = Boton(list(cardPlayed.keys())[0], cardPlayedOP, posX, posY, width, height)
        
        # Se requiere dos loops para este código. Uno actualiza la carta jugada y el otro espera la respuesta del 
        # jugador. Esta variable es para este último.
        nextPlay = False

        # Cuando el mazo del jugador sólo posea una carta, si el jugador juega esa carta y no presiona el botón uno, se
        # le añadirá otra carta.
        if len(mazoPlayerList[actualPlayer]) < 1 and not buttomPressed[actualPlayer]:
            deckCard.addCard(mazoPlayerList[actualPlayer], mazoOPPlayerList[actualPlayer])

            minimizeWindow()
            isVideo("./esthetic/blockCard.webm")
            isVideo("./esthetic/sigTurn.webm")
            restoreWindow(screenSize)

            nextPlay = True
            actualPlayer+= ((1*playDirection))
        # Si se ha presionado el botón, entonces el jugador habrá ganado.
        elif len(mazoPlayerList[actualPlayer-1]) < 1 and buttomPressed[actualPlayer-1]:
            minimizeWindow()
            if actualPlayer-1 == 0:
                isVideo("./esthetic/win1.webm")
                winPlayer = 1
            else:
                isVideo("./esthetic/win2.webm")
                winPlayer = 2
            restoreWindow(screenSize)
            nextPlay = gameOver = True
        
        # El segundo ciclo que se mencionó anteriormente. Este es encargado de las respuestas que de el jugador.
        while not nextPlay:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    nextPlay = True
                    gameOver = True 

            # Se visualiza el tablero.
            screen.blit(tablero, (0, 0))

            if dealCardsCounter < 2 and validDeal:
                sleep(0.1)

            # Se actualiza el botón uno y detecta si hay pulsaciones.
            unoButtom.update(screen, cursor)
            if len(mazoPlayerList[actualPlayer])==1:
                if cursor.colliderect(unoButtom.rect) and pg.mouse.get_pressed()[0]:
                    buttomPressed[actualPlayer] = True
            else:
                buttomPressed[actualPlayer] = False

            #Indicador de jugador en juego. En un principio era temporal pero se terminó quedando.
            screen.blit(((imgPlayer1) if actualPlayer%2==0 else (imgPlayer2)), (0, 0))

            # Si el jugador, aunque tenga cartas en juego, decide presionar el boton "Tomar carta", no se le negará su 
            # capricho.
            cardTakenButtom.update(screen, cursor)
            if cursor.colliderect(cardTakenButtom.rect) and pg.mouse.get_pressed()[0] and allCardsTaken:
                dealCard.play()
                deckCard.addCard(mazoPlayerList[actualPlayer], mazoOPPlayerList[actualPlayer])
                nextPlay = True
                actualPlayer+= (1*playDirection)
                minimizeWindow()
                isVideo("./esthetic/sigTurn.webm")
                restoreWindow(screenSize)
                
            # Se actualiza el cursor.
            cursor.update()

            # Se muestra en pantalla la carta que está en juego.
            figurePlayed.update(screen, cursor, False)

            # Se muestra en pantalla la baraja del jugador
            paramsFunct = (mazoPlayerList, actualPlayer,
                mazoOPPlayerList, screenSize, width, height,
                initIndex, screen, cursor, rightArrowButtom, leftArrowButtom, dealCardsCounter,
                validDeal, dealCard, cardPlayed, frameCardOP, frameCard, frames, fps, nextPlay)
            nextPlay, initIndex, imgDeckPlayer, dealCardsCounter, actualPlayer = refreshDeck(*paramsFunct)
            validDeal = False
                
            # Se vuelve a actualizar el cursor.
            cursor.update()
            # Si la carta en juego es block, se le negará al siguiente jugador la pobilidad de juego.
            blockCounter,isBlockCard = blockCard(cardPlayed, blockCounter)
            if isBlockCard and allCardsTaken:
                
                nextPlay = True

                # Ahora la carta jugada sólo tendrá su color.
                cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).keys())[0]
                
                actualPlayer += (1*playDirection)

                minimizeWindow()
                isVideo("./esthetic/blockCard.webm")
                isVideo("./esthetic/sigTurn.webm")
                restoreWindow(screenSize)

            else:
                # Si la carta en juego es reverse, se cambia la dirección de juego.
                reverseCounter, isReverseCard = reverseCard(cardPlayed, reverseCounter)
                if isReverseCard and allCardsTaken:
                    dealCardsCounter += 1
                    playDirection *= -1
                    actualPlayer += (1*playDirection)
                    # Ahora la carta jugada sólo tendrá su color.
                    cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).keys())[0]
                    nextPlay = validDeal = True

                    minimizeWindow()
                    isVideo("./esthetic/reverseCard.webm")
                    isVideo("./esthetic/sigTurn.webm")
                    restoreWindow(screenSize)
                
                # Si la carta en juego es change color, se pedirá al jugador seleccionar un color.
                elif changeColor(cardPlayed) and allCardsTaken and not (isPlusFour(cardPlayed)):
                    # La carta jugada será equivalente a lo que retorne la función selColor.
                    try:
                        if not ("+2" in list(dict(list(cardPlayed.values())[0]).values())[0]):
                            cardPlayed = selColor(cardPlayed)
                    except:
                        cardPlayed = selColor(cardPlayed)
                    nextPlay =  validDeal = True
                    dealCardsCounter += 1
                    actualPlayer += (1*playDirection)
                    sleep(0.1)
                    
                    minimizeWindow()
                    isVideo("./esthetic/sigTurn.webm")
                    restoreWindow(screenSize)

                # Si la carta en juego es "+4", se le pedirá al jugador seleccionar un color.
                elif isPlusFour(cardPlayed) and not ("+4" == list(cardPlayed.values())[0]):
                    # La carta jugada será equivalente a lo que retorne la función selColor con el parámetro opcional 
                    # en True.
                    cardPlayed = selColor(cardPlayed, True)

                    nextPlay =  validDeal = True
                    dealCardsCounter += 1
                    actualPlayer += (1*playDirection)
                    sleep(0.1)
                    
                    minimizeWindow()
                    isVideo("./esthetic/sigTurn.webm")
                    restoreWindow(screenSize)

                # Si el jugador tiene por lo menos una carta igual, esta función la reconocerá y hará que se quede esperando la respuesta del jugador.
                elif findEqualCard(mazoPlayerList[actualPlayer], cardPlayed) and allCardsTaken:
                    for index in range(len(imgDeckPlayer)):
                        element = imgDeckPlayer[index]
                        # Si esa carta válida es presionada, se retira de la baraja del jugador y se pone en juego.
                        if cursor.colliderect(element.rect) and pg.mouse.get_pressed()[0] and isEqual(mazoPlayerList[actualPlayer][initIndex + index], cardPlayed):
                            dealCard.play()
                            cardPlayed = mazoPlayerList[actualPlayer][initIndex+index]
                            mazoPlayerList[actualPlayer].pop(initIndex+index)
                            mazoOPPlayerList[actualPlayer].pop(initIndex+index)
                            minimizeWindow()
                            try:
                                if not ("change color" in list(cardPlayed.values())[0].lower()):
                                    isVideo("./esthetic/sigTurn.webm")
                                # Si es +4, se añadirá al contador cartas a tomar.
                                if isPlusFour(cardPlayed):
                                    cardTakenCounter += 4
                            except:
                                isVideo("./esthetic/sigTurn.webm")
                                if isPlusFour(cardPlayed):
                                    cardTakenCounter += 4
                                else:
                                    try:
                                        if "+2" in list(dict(list(cardPlayed.values())[0]).values())[0]:
                                            cardTakenCounter += 2
                                    except:
                                        pass
                            restoreWindow(screenSize)
                                
                            blockCounter += 1
                            reverseCounter += 1
                            actualPlayer += (1*playDirection)
                            
                            dealCardsCounter += 1
                            nextPlay = validDeal = True
                            sleep(0.1)
                # Si los anteriores bloques de código no concluyeron en nada, el jugador no posee una carta en juego y, 
                # por tanto, tendrá que tomar carta.
                else:
                    if noCardCounter==0:
                        noCardCounter+=1
                        allCardsTaken = False
                    
                    Boton(frameCardOP, frameCard, 50, 60, width, height)
                    cardTakenButtom.update(screen, cursor)
                    if cursor.colliderect(cardTakenButtom.rect) and pg.mouse.get_pressed()[0]:
                        cardsTaken += 1
                        if "+4" in list(cardPlayed.values())[0]:
                            # Si la última carta es +4, al tomar la última carta del contador se cambiará su valor a 
                            # únicamente el color.
                            if cardTakenCounter == cardsTaken:
                                cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).values())[0]
                        else:
                            # Si la última carta es +2, al tomar la última carta del contador se cambiará su valor a 
                            # únicamente el color.
                            try:
                                if "+2" in list(dict(list(cardPlayed.values())[0]).values())[0]:
                                    if cardTakenCounter == cardsTaken:
                                        cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).keys())[0]
                                else:
                                    cardTakenCounter = 1
                                    
                            except:
                                cardTakenCounter = 1
                        # Se van añádiendo cartas como también actualizando la baraja hasta que el contador de cartas 
                        # tomadas sea igual a cartas a tomar
                        dealCard.play()
                        nextPlay = True
                        deckCard.addCard(mazoPlayerList[actualPlayer], mazoOPPlayerList[actualPlayer])
                        if cardsTaken == cardTakenCounter:
                            minimizeWindow()
                            isVideo("./esthetic/sigTurn.webm")
                            restoreWindow(screenSize)
                            cardsTaken = cardTakenCounter = noCardCounter = 0
                            actualPlayer += (1*playDirection)
                            blockCounter += 1
                            reverseCounter += 1
                            dealCardsCounter += 1
                            allCardsTaken = validDeal =  True
                        sleep(0.1)

            refreshScreen(frames, fps)
        refreshScreen(frames, fps)
    # Si se cierra el juego abruptamente, no se mostrará en la pantalla algún jugador ganador.
    if not gameOver:
        # Se muestra en la pantalla aquel jugador que ganó.
        imgPlayerWin = Boton("./esthetic/Win{0}.png".format(winPlayer), "./esthetic/Win{0}.png".format(winPlayer), 0, 0, 960, 640)

        closeWindow = False
        while not closeWindow:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    closeWindow = True
            
            imgPlayerWin.update(screen, cursor, False)


    pg.mouse.set_visible(1)
    return 0


