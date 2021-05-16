import pygame as pg
from buttoms import Boton
from mouse import Cursor
from movies import isVideo

def selColor(cardPlayed, conditional:bool=False):
    pg.init()

    # Screen
    screenSize = (960, 640)
    screen = pg.display.set_mode(screenSize)

    # FPS
    frames = pg.time.Clock()
    fps = 60

    # imgBackground
    background = pg.transform.scale(pg.image.load("./esthetic/Escoge.png"), screenSize)


    # Width - heigth buttoms
    width = 350
    height = 80
    # buttomRed
    redB = pg.transform.scale(pg.image.load("./esthetic/Rojo.png"), (width, height))
    redBOp = pg.transform.scale(pg.image.load("./esthetic/RojoOp.png"), (width, height))

    # ButtomBlue
    blueB = pg.transform.scale(pg.image.load("./esthetic/Azul.png"), (width, height))
    blueBOp = pg.transform.scale(pg.image.load("./esthetic/AzulOp.png"), (width, height))

    # ButtomGreen
    greenB = pg.transform.scale(pg.image.load("./esthetic/Verde.png"), (width, height))
    greenBOp = pg.transform.scale(pg.image.load("./esthetic/VerdeOp.png"), (width, height))

    # ButtomYellow
    yellowB = pg.transform.scale(pg.image.load("./esthetic/Amarillo.png"), (width, height))
    yellowBOp = pg.transform.scale(pg.image.load("./esthetic/AmarilloOp.png"), (width, height))

    # Pos buttoms
    xPos = screenSize[0]//2-width//2
    yPos = screenSize[1]//4

    # Mouse
    mousePoint = Cursor()

    # Buttoms
    rBot = Boton(redB, redBOp, xPos, yPos)
    bBot = Boton(blueB, blueBOp, xPos, yPos + 3*height//2)
    gBot = Boton(greenB, greenBOp, xPos, yPos + 3*height)
    yBot = Boton(yellowB, yellowBOp, xPos, yPos + 9*height//2)

    while True:
        screen.blit(background, (0, 0))

        rBot.update(screen, mousePoint)
        bBot.update(screen, mousePoint)
        gBot.update(screen, mousePoint)
        yBot.update(screen, mousePoint)
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if mousePoint.colliderect(rBot.rect):
                    isVideo("./esthetic/esRojo.webm", 0, 0)
                    return ({list(cardPlayed.keys())[0]:{"+4": "Red"}} if conditional else {list(cardPlayed.keys())[0]:"Red"})
                elif mousePoint.colliderect(bBot.rect):
                    isVideo("./esthetic/esAzul.webm", 0, 0)
                    return ({list(cardPlayed.keys())[0]:{"+4": "Blue"}} if conditional else {list(cardPlayed.keys())[0]:"Blue"})
                elif mousePoint.colliderect(gBot.rect):
                    isVideo("./esthetic/esVerde.webm", 0, 0)
                    return ({list(cardPlayed.keys())[0]:{"+4": "Green"}} if conditional else {list(cardPlayed.keys())[0]:"Green"})
                elif mousePoint.colliderect(yBot.rect):
                    isVideo("./esthetic/esAmarillo.webm", 0, 0)
                    return ({list(cardPlayed.keys())[0]:{"+4": "Yellow"}} if conditional else {list(cardPlayed.keys())[0]:"Yellow"})
        mousePoint.update()
        pg.display.flip()
        frames.tick(fps)
