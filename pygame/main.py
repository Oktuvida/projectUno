
import pygame as pg 
from deck import deckCards
from player import jugador
from time import sleep
from moves import isEqual, findEqualCard, changeColor, isPlusFour, blockCard, reverseCard
from selectColor import selColor
from mouse import Cursor
from movies import isVideo
from buttoms import Boton

def refreshScreen(frames, fps):
    pg.display.flip()
    frames.tick(fps)

def refreshDeck(mazoPlayerList, actualPlayer, mazoOPPlayerList, screenSize, width, height,
    initIndex, screen, cursor, rightArrowButtom, leftArrowButtom, dealCardsCounter,
    validDeal, dealCard, cardPlayed, frameCardOP, frameCard, frames, fps, nextPlay):
    if actualPlayer > len(mazoPlayerList)-1:
        actualPlayer = 0
    elif actualPlayer < 0:
        actualPlayer = len(mazoPlayerList)-1
    cursor.update()
    xPos = screenSize[0]//5-width
    yPos = screenSize[0]//2+height//6
    deckPlayer = []
    for element1, element2 in zip(mazoPlayerList[actualPlayer], mazoOPPlayerList[actualPlayer]):            
        deckPlayer.append(Boton(element2,list(element1.keys())[0], xPos, yPos, width//2, height//2))
        xPos += width
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
    xPos = screenSize[0]//5-width
    yPos = screenSize[0]//2+height//6
    imgDeckPlayer = []
    for element in deckPlayer[initIndex:initIndex+7]:
        if dealCardsCounter < 2 and validDeal:
            try:
                if not ("change color" in list(cardPlayed.values())[0].lower()):
                    dealCard.play()
                else:
                    dealCardsCounter -= 1
            except:
                dealCard.play()
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
    
    cardTakenCounter = 0
    cardsTaken = 0

    noCardCounter = 0


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

    # Is next play.
    allCardsTaken = True
    gameOver = False

    # See cards
    #seeCards = True

    # Music
    ambientSound = pg.mixer.music
    ambientSound.load("./music/ambient.mp3")
    ambientSound.set_volume(0.05)
    ambientSound.play()

    shuffleSound = pg.mixer.Sound("./music/barajar.wav")
    dealCard = pg.mixer.Sound("./music/repartir.wav")

    dealCardsCounter = 0
    validDeal = True

    shuffleSound.play()
    while not gameOver:
        if actualPlayer > len(mazoPlayerList)-1:
            actualPlayer = 0
        elif actualPlayer < 0:
            actualPlayer = len(mazoPlayerList)-1
        #Carta jugada
        figurePlayed = Boton(list(cardPlayed.keys())[0], cardPlayedOP, posX, posY, width, height)
        
        nextPlay = False

        if len(mazoPlayerList[actualPlayer]) < 1 and not buttomPressed[actualPlayer]:
            deckCard.addCard(mazoPlayerList[actualPlayer], mazoOPPlayerList[actualPlayer])

            minimizeWindow()
            isVideo("./esthetic/blockCard.webm")
            isVideo("./esthetic/sigTurn.webm")
            restoreWindow(screenSize)

            nextPlay = True
            actualPlayer+= ((1*playDirection))
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
        

        while not nextPlay:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    nextPlay = True
                    gameOver = True 

            # Fondo
            screen.blit(tablero, (0, 0))

            if dealCardsCounter < 2 and validDeal:
                sleep(0.1)

            unoButtom.update(screen, cursor)
            if len(mazoPlayerList[actualPlayer])==1:
                if cursor.colliderect(unoButtom.rect) and pg.mouse.get_pressed()[0]:
                    buttomPressed[actualPlayer] = True
            else:
                buttomPressed[actualPlayer] = False
            #Indicador de jugador en juego
            screen.blit(((imgPlayer1) if actualPlayer%2==0 else (imgPlayer2)), (0, 0))

            cardTakenButtom.update(screen, cursor)
            if cursor.colliderect(cardTakenButtom.rect) and pg.mouse.get_pressed()[0] and allCardsTaken:
                dealCard.play()
                deckCard.addCard(mazoPlayerList[actualPlayer], mazoOPPlayerList[actualPlayer])
                nextPlay = True
                actualPlayer+= (1*playDirection)
                minimizeWindow()
                isVideo("./esthetic/sigTurn.webm")
                restoreWindow(screenSize)
                

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
                

            cursor.update()
            blockCounter,isBlockCard = blockCard(cardPlayed, blockCounter)
            if isBlockCard and allCardsTaken:
                
                nextPlay = True


                cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).keys())[0]
                
                actualPlayer += (1*playDirection)

                minimizeWindow()
                isVideo("./esthetic/blockCard.webm")
                isVideo("./esthetic/sigTurn.webm")
                restoreWindow(screenSize)

            else:
                reverseCounter, isReverseCard = reverseCard(cardPlayed, reverseCounter)
                if isReverseCard and allCardsTaken:
                    dealCardsCounter += 1
                    playDirection *= -1
                    actualPlayer += (1*playDirection)
                    cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).keys())[0]
                    nextPlay = validDeal = True

                    minimizeWindow()
                    isVideo("./esthetic/reverseCard.webm")
                    isVideo("./esthetic/sigTurn.webm")
                    restoreWindow(screenSize)
                
                elif changeColor(cardPlayed) and allCardsTaken and not (isPlusFour(cardPlayed)):
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

                    
                elif isPlusFour(cardPlayed) and not ("+4" == list(cardPlayed.values())[0]):
                    cardPlayed = selColor(cardPlayed, True)

                    nextPlay =  validDeal = True
                    dealCardsCounter += 1
                    actualPlayer += (1*playDirection)
                    sleep(0.1)
                    
                    minimizeWindow()
                    isVideo("./esthetic/sigTurn.webm")
                    restoreWindow(screenSize)

                elif findEqualCard(mazoPlayerList[actualPlayer], cardPlayed) and allCardsTaken:
                    for index in range(len(imgDeckPlayer)):
                        element = imgDeckPlayer[index]
                        if cursor.colliderect(element.rect) and pg.mouse.get_pressed()[0] and isEqual(mazoPlayerList[actualPlayer][initIndex + index], cardPlayed):
                            dealCard.play()
                            cardPlayed = mazoPlayerList[actualPlayer][initIndex+index]
                            mazoPlayerList[actualPlayer].pop(initIndex+index)
                            mazoOPPlayerList[actualPlayer].pop(initIndex+index)
                            minimizeWindow()
                            try:
                                if not ("change color" in list(cardPlayed.values())[0].lower()):
                                    isVideo("./esthetic/sigTurn.webm")
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
                        
                else:
                    if noCardCounter==0:
                        noCardCounter+=1
                        allCardsTaken = False
                        
                    Boton(frameCardOP, frameCard, 50, 60, width, height)
                    cardTakenButtom.update(screen, cursor)
                    if cursor.colliderect(cardTakenButtom.rect) and pg.mouse.get_pressed()[0]:
                        cardsTaken += 1
                        if "+4" in list(cardPlayed.values())[0]:
                            if cardTakenCounter == cardsTaken:
                                cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).values())[0]
                        else:
                            try:
                                if "+2" in list(dict(list(cardPlayed.values())[0]).values())[0]:
                                    if cardTakenCounter == cardsTaken:
                                        cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).keys())[0]
                                else:
                                    cardTakenCounter = 1
                                    
                            except:
                                cardTakenCounter = 1
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

    if not gameOver:
        imgPlayerWin = Boton("./esthetic/Win{0}.png".format(winPlayer), "./esthetic/Win{0}.png".format(winPlayer), 0, 0, 960, 640)

        closeWindow = False
        while not closeWindow:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    closeWindow = True
            
            imgPlayerWin.update(screen, cursor, False)


    pg.mouse.set_visible(1)
    return 0


