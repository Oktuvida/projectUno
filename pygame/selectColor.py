import pygame as pg
from buttoms import Boton
from mouse import Cursor
from movies import isVideo

# La clase selColor inicia una pantalla en Pygame mostrando un color a mostrar.
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
    redB = "./esthetic/Rojo.png"
    redBOp = "./esthetic/RojoOp.png"

    # ButtomBlue
    blueB = "./esthetic/Azul.png"
    blueBOp = "./esthetic/AzulOp.png"

    # ButtomGreen
    greenB = "./esthetic/Verde.png"
    greenBOp = "./esthetic/VerdeOp.png"

    # ButtomYellow
    yellowB = "./esthetic/Amarillo.png"
    yellowBOp = "./esthetic/AmarilloOp.png"

    # Pos buttoms
    xPos = screenSize[0]//2-width//2
    yPos = screenSize[1]//4

    # Mouse
    mousePoint = Cursor()

    # Buttoms
    rBot = Boton(redB, redBOp, xPos, yPos, width, height)
    bBot = Boton(blueB, blueBOp, xPos, yPos + 3*height//2, width, height)
    gBot = Boton(greenB, greenBOp, xPos, yPos + 3*height, width, height)
    yBot = Boton(yellowB, yellowBOp, xPos, yPos + 9*height//2, width, height)

    while True:
        screen.blit(background, (0, 0))

        rBot.update(screen, mousePoint)
        bBot.update(screen, mousePoint)
        gBot.update(screen, mousePoint)
        yBot.update(screen, mousePoint)
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                # Según el color que sea seleccionado se retornará el valor de la carta jugada, modificando únicamente 
                # los values iniciales.
                if mousePoint.colliderect(rBot.rect):
                    isVideo("./esthetic/esRojo.webm")
                    return ({list(cardPlayed.keys())[0]:{"+4": "Red"}} if conditional else {list(cardPlayed.keys())[0]:"Red"})
                elif mousePoint.colliderect(bBot.rect):
                    isVideo("./esthetic/esAzul.webm")
                    return ({list(cardPlayed.keys())[0]:{"+4": "Blue"}} if conditional else {list(cardPlayed.keys())[0]:"Blue"})
                elif mousePoint.colliderect(gBot.rect):
                    isVideo("./esthetic/esVerde.webm")
                    return ({list(cardPlayed.keys())[0]:{"+4": "Green"}} if conditional else {list(cardPlayed.keys())[0]:"Green"})
                elif mousePoint.colliderect(yBot.rect):
                    isVideo("./esthetic/esAmarillo.webm")
                    return ({list(cardPlayed.keys())[0]:{"+4": "Yellow"}} if conditional else {list(cardPlayed.keys())[0]:"Yellow"})
        mousePoint.update()
        pg.display.flip()
        frames.tick(fps)
