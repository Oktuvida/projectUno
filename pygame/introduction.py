import pygame as pg
from main import game
from time import sleep
from os import environ, getcwd
from buttoms import Boton
from mouse import Cursor

        
        
def introduction(): 
    environ["SDL_VIDEO_WINDOW_POS"] = "0, 0"
    pg.init()           #Inicializamos módulo
    x = 960
    y = 640
    ventana = pg.display.set_mode((x, y))   #Le damos un tamaño a la ventana
    pg.display.set_caption("¡Uno!")  #Le damos un nombre a la ventana
    
    Pinicio = pg.image.load("pygame/imgIntroduction/pantallaInicio.jpg")
    PinicioEscala = pg.transform.scale(Pinicio, (x, y))
    jugar1 = "pygame/imgIntroduction/jugar12.jpg"
    jugar2 = "pygame/imgIntroduction/jugar22.jpg"
    instrucciones1 = "pygame/imgIntroduction/instrucciones1.jpg"
    instrucciones2 = "pygame/imgIntroduction/instrucciones2.jpg"
    fondInstruc = pg.transform.scale(pg.image.load("./esthetic/Instrucciones.png"), (x, y))
    #lArrow = pg.transform.flip(pg.transform.scale("./esthetic/Fde.png"), (50, 50)), True, False)
    lArrow = "./esthetic/Fde.png"
    #lArrowOp = pg.transform.scale("./esthetic/Fizop.png"), (50, 50))
    lArrowOp = "./esthetic/Fdeop.png"
    counter = 0


    reloj1 = pg.time.Clock()

    boton1 = Boton(jugar1, jugar2, x//2-125, y//2+25)
    boton2 = Boton(instrucciones1, instrucciones2, x//2-125, y//2+125)
    boton3 = Boton(lArrow, lArrowOp, 75, 50, 50, 50, True)


    cursor1 = Cursor()

    Game_over = False            #Loop infinito   
    while Game_over != True:   
              
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                        game()
                    if cursor1.colliderect(boton2.rect):
                        ventana.blit(fondInstruc, (0, 0))
                        boton3.update(ventana, cursor1)
                        counter = 1
                        
            if event.type == pg.QUIT:  
                Game_over = True
        if counter%2!=0:
            boton3.update(ventana, cursor1) 
            if cursor1.colliderect(boton3.rect):
                boton3.update(ventana, cursor1)
                if pg.mouse.get_pressed()[0]:
                    counter = 0
        if counter%2 == 0:
            ventana.blit(PinicioEscala, (0, 0))  
            boton1.update(ventana, cursor1)
            boton2.update(ventana, cursor1)
        cursor1.update()
        
        reloj1.tick(20)
        pg.display.flip()

    #pygame.display.flip()
    pg.quit()

if __name__ == "__main__":  
    print(getcwd())
    introduction()