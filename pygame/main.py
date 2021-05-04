import pygame as pg 
from deck import deckCards
from player import jugador
from random import randint
from time import sleep
from moves import isEqual, findEqualCard

def game ():
    pg.init()

    #colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)


    #Fotogramas
    frames = pg.time.Clock()
    fps = 60

    screenSize = (800, 600)
    screen = pg.display.set_mode(screenSize)

    #rect
    posX = (screenSize[0]//2)-50
    posY = screenSize[1]//3 - 82
    width = 100
    height = 165

    

    #Baraja de cartas
    deckCard = deckCards()

    #Jugadores
    player1 = jugador(deckCard)
    mazoP1 = player1.mazo

    #Arrows to watch deck
    initIndex = 0
    rightArrow = pg.transform.scale(pg.image.load("pygame/imgArrow/rightArrow.png"), (50, 50))
    leftArrow = pg.transform.flip(rightArrow, True, False)

    #Counter +4 or change color
    #Mouse
    pg.mouse.set_visible(0)
    cardPlayed = deckCard.selectCard()
    gameOver = False
    while not gameOver:        
        #Carta jugada
        figurePlayed = pg.transform.scale(pg.image.load(list(cardPlayed.keys())[0]), (width, height))
        #Baraja jugador
        deckPlayer = []
        for element in mazoP1:
            deckPlayer.append(pg.transform.scale(pg.image.load(list(element.keys())[0]), (width//2, height//2)))

        
        nextPlay = False
        while not nextPlay:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    nextPlay = True
                    gameOver = True 

            mousePos = pg.mouse.get_pos()

            xPos = 90
            yPos = 450


            screen.fill(black)
            

            rect = (mousePos[0], mousePos[1], 15, 15)
            mousePoint = pg.draw.rect(screen, white, rect)

            if len(deckPlayer)>7:
                if initIndex+7<len(deckPlayer):
                    rArrow = screen.blit(rightArrow, (750, 470))
                    if mousePoint.colliderect(rArrow) and pg.mouse.get_pressed()[0]:
                        initIndex+=1
                        nextPlay=True
                        sleep(0.1)
                if initIndex-1 >= 0:
                    lArrow = screen.blit(leftArrow, (30, 470))
                    if mousePoint.colliderect(lArrow) and pg.mouse.get_pressed()[0]:
                        initIndex-=1
                        nextPlay=True
                        sleep(0.1)

            imgDeckPlayer = []
            for element in deckPlayer[initIndex:initIndex+7]:
                if isEqual(mazoP1[deckPlayer.index(element)], cardPlayed):
                    pg.draw.rect(screen, red, (xPos-1, yPos-1, width//1.9, height//1.9))
                imgDeckPlayer.append(screen.blit(element, (xPos, yPos)))
                xPos += 100

            screen.blit(figurePlayed, (posX, posY))

            rect = (mousePos[0], mousePos[1], 15, 15)
            mousePoint = pg.draw.rect(screen, white, rect)

            if findEqualCard(mazoP1, cardPlayed) == True:
                for index in range(len(imgDeckPlayer)):
                    element = imgDeckPlayer[index]
                    if mousePoint.colliderect(element) and pg.mouse.get_pressed()[0] and isEqual(mazoP1[initIndex + index], cardPlayed):
                        cardPlayed = mazoP1[initIndex+index]
                        mazoP1.pop(initIndex+index)
                        nextPlay = True
                        sleep(0.1)
            else:
                deckCard.addCard(mazoP1)
                nextPlay = True
                sleep(0.1)

            pg.display.flip()
            frames.tick(fps)
    #pg.quit()