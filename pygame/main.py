import pygame as pg 
from deck import deckCards
from player import jugador
from random import randint
from time import sleep
from moves import isEqual, findEqualCard, changeColor, isPlusFour, blockCard, reverseCard
from selectColor import selColor
from mouse import Cursor
from movies import isVideo

def game ():
    #Posición de ventana
    pg.init()

    #colors
    red = (255, 0, 0)
    
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
    
    player2 = jugador(deckCard)
    mazoP2 = player2.mazo

    #playerList = [player1, player2]
    mazoPlayerList = [mazoP1, mazoP2]

    # Player active
    actualPlayer = 0

    #Arrows to watch deck
    initIndex = 0
    rightArrow = pg.transform.scale(pg.image.load("./esthetic/Fde.png"), (50, 50))
    leftArrow = pg.transform.flip(rightArrow, True, False)
    rightArrowOp = pg.transform.scale(pg.image.load("./esthetic/Fdeop.png"), (50, 50))
    leftArrowOp = pg.transform.flip(rightArrowOp, True, False)

    #Mouse
    cursor = Cursor()

    #cardTaken
    cardTaken = pg.transform.scale(pg.image.load("./esthetic/Cartare.png"), (width, height))
    
    cardTakenCounter = 0
    cardsTaken = 0

    noCardCounter = 0

    #Carta jugada
    cardPlayed = deckCard.selectCard()

    #Counter Block card
    blockCounter = 0
    isBlockCard = False

    

    #Reverse Block card
    reverseCounter = 0
    isReverseCard = False

    # Is next play.
    validPlay = bool()

    gameOver = False
    while not gameOver:        
        validPlay = False
        if actualPlayer > len(mazoPlayerList)-1:
            actualPlayer = 0
        if actualPlayer < 0:
            actualPlayer = len(mazoPlayerList)-1
        #Carta jugada
        figurePlayed = pg.transform.scale(pg.image.load(list(cardPlayed.keys())[0]), (width, height))
        #Baraja jugador
        deckPlayer = []
        for element in mazoPlayerList[actualPlayer]:
            deckPlayer.append(pg.transform.scale(pg.image.load(list(element.keys())[0]), (width//2, height//2)))
        
        nextPlay = False
        while not nextPlay:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    nextPlay = True
                    gameOver = True 

            xPos = screenSize[0]//5-width
            yPos = screenSize[0]//2+height//6

            # Fondo
            screen.blit(tablero, (0, 0))

            #Baraja a tomar
            imgCardTaken = screen.blit(cardTaken, (50, 40))

            cursor.update()

            if len(deckPlayer)>7:
                if initIndex+7<len(deckPlayer):
                    rArrow = screen.blit(rightArrow, (screenSize[0]-55, screenSize[1]-100))
                    if cursor.colliderect(rArrow):
                        rArrow = screen.blit(rightArrowOp, (screenSize[0]-55, screenSize[1]-100))
                        if pg.mouse.get_pressed()[0]:
                            initIndex+=1
                            nextPlay=True
                            sleep(0.1)
                if initIndex-1 >= 0:
                    lArrow = screen.blit(leftArrow, (5, screenSize[1]-100))
                    if cursor.colliderect(lArrow):
                        lArrow = screen.blit(leftArrowOp, (5, screenSize[1]-100))
                        if pg.mouse.get_pressed()[0]:
                            initIndex-=1
                            nextPlay=True
                            sleep(0.1)

            imgDeckPlayer = []
            for element in deckPlayer[initIndex:initIndex+7]:
                if isEqual(mazoPlayerList[actualPlayer][deckPlayer.index(element)], cardPlayed):
                    pg.draw.rect(screen, red, (xPos-1, yPos-1, width//1.9, height//1.9))
                imgDeckPlayer.append(screen.blit(element, (xPos, yPos)))
                xPos += width

            screen.blit(figurePlayed, (posX, posY))

            cursor.update()

            sleep(0.1)
            if changeColor(cardPlayed):
                if "+4" in list(cardPlayed.values())[0]:
                    cardPlayed = selColor(cardPlayed, True)
                else:
                    cardPlayed = selColor(cardPlayed)
                nextPlay = validPlay = True

            else:
                blockCounter,isBlockCard = blockCard(cardPlayed, blockCounter)
                if isBlockCard:
                    actualPlayer += 1
                    nextPlay = validPlay = True
                else:
                    reverseCounter, isReverseCard = reverseCard(cardPlayed, reverseCounter)
                    if isReverseCard:
                        actualPlayer -= 1
                        nextPlay = validPlay = True
                    elif findEqualCard(mazoPlayerList[actualPlayer], cardPlayed):
                        for index in range(len(imgDeckPlayer)):
                            element = imgDeckPlayer[index]
                            if cursor.colliderect(element) and pg.mouse.get_pressed()[0] and isEqual(mazoPlayerList[actualPlayer][initIndex + index], cardPlayed):
                                cardPlayed = mazoPlayerList[actualPlayer][initIndex+index]
                                mazoPlayerList[actualPlayer].pop(initIndex+index)
                                actualPlayer += 1
                                try:
                                    if not ("change color" in list(cardPlayed.values())[0].lower()):
                                        validPlay = True
                                except:
                                    validPlay = True
                                nextPlay = True
                                blockCounter += 1
                                reverseCounter += 1
                                sleep(0.1)
                            
                    else:
                        if noCardCounter==0:
                            isVideo("./esthetic/noCard.webm", 0, 0)
                            noCardCounter+=1
                        pg.draw.rect(screen, red, pg.Rect(50-2, 40-2, width+4, height+4))
                        imgCardTaken = screen.blit(cardTaken, (50, 40))
                        if cursor.colliderect(imgCardTaken) and pg.mouse.get_pressed()[0]:
                            if "+4" in list(cardPlayed.values())[0]:
                                cardTakenCounter = 4
                                if cardTakenCounter == cardsTaken:
                                    cardPlayed[list(cardPlayed.keys())[0]] = list(dict(list(cardPlayed.values())[0]).values())[0]
                            elif "+2" in list(cardPlayed.values())[0]:
                                cardTakenCounter = 2
                                if cardTakenCounter == cardsTaken:
                                    cardPlayed[cardPlayed.keys()[0]] = list(dict(list(cardPlayed.values())[0]).keys())[0]
                            nextPlay = True
                            deckCard.addCard(mazoPlayerList[actualPlayer])
                            cardsTaken += 1
                            if cardTakenCounter == cardsTaken:
                                validPlay = True
                                actualPlayer += 1
                                blockCounter += 1
                                reverseCounter += 1
                                noCardCounter = 0
                            sleep(0.1)

            pg.display.flip()
            frames.tick(fps)
        if not gameOver and validPlay:
            isVideo("./esthetic/sigTurn.webm", 0, 0)
            cardsTaken = 0
            
        pg.display.flip()
        frames.tick(fps)
        
        if not gameOver:
            sleep(0.1)
    
    pg.mouse.set_visible(1)
    return 0