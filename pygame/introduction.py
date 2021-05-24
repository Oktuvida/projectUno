import pygame as pg
from main import game
from time import sleep
from os import environ
from buttoms import Boton
from mouse import Cursor

        
# Función que da bienvenida al jugador.        
def introduction(): 
    # Función que posiciona la ventana de pygame
    environ["SDL_VIDEO_WINDOW_POS"] = "0, 0"
    pg.init()           #Inicializamos módulo
    x = 960
    y = 640
    ventana = pg.display.set_mode((x, y))   #Le damos un tamaño a la ventana
    pg.display.set_caption("¡Uno!")  #Le damos un nombre a la ventana

    # Se recolecta, en algunos casos,los path de las imagenes, y en otros, se inicializa una imagen.
    Pinicio = pg.image.load("pygame/imgIntroduction/pantallaInicio.jpg")
    PinicioEscala = pg.transform.scale(Pinicio, (x, y))
    jugar1 = "pygame/imgIntroduction/jugar12.jpg"
    jugar2 = "pygame/imgIntroduction/jugar22.jpg"
    instrucciones1 = "pygame/imgIntroduction/instrucciones1.jpg"
    instrucciones2 = "pygame/imgIntroduction/instrucciones2.jpg"
    fondInstruc = pg.transform.scale(pg.image.load("./esthetic/Instrucciones.png"), (x, y))
    lArrow = "./esthetic/Fde.png"
    lArrowOp = "./esthetic/Fdeop.png"
    counter = 0

    # La tasa de fotogramas por segundo.
    reloj1 = pg.time.Clock()

    # Se inicializa la clase Boton con los anteriores path.
    boton1 = Boton(jugar1, jugar2, x//2-125, y//2+25)
    boton2 = Boton(instrucciones1, instrucciones2, x//2-125, y//2+125)
    boton3 = Boton(lArrow, lArrowOp, 75, 50, 50, 50, True)

    # Se inicializa el cursor.
    cursor1 = Cursor()

    Game_over = False            #Loop infinito   
    while Game_over != True:   
              
        # Ciclo encargado de registrar los eventos en pygame
        for event in pg.event.get():
            # Evento que se encarga de recoger las pulsaciones del mouse. En otros archivos se usa la función pygame.
            # mouse.get_pressed()[0]
            if event.type == pg.MOUSEBUTTONDOWN:
                    # Pulsación que se encarga del botón "Iniciar juego"
                    if cursor1.colliderect(boton1.rect):
                        game()
                    # Pulsación que se encarga del botón "intrucciones"
                    if cursor1.colliderect(boton2.rect):
                        ventana.blit(fondInstruc, (0, 0))
                        boton3.update(ventana, cursor1)
                        # Contador de pulsaciones. Si está en 1, permanecerá en la ventana de intrucciones.
                        counter = 1
            # Cuando se presiona el botón de cerrar pestaña, será este el encargado de registrarlo y ejecutarlo.
            if event.type == pg.QUIT:  
                Game_over = True

        # Bloque de código cuando se está en intrucciones. Se inicializa un nuevo botón para retroceder.
        if counter%2!=0:
            boton3.update(ventana, cursor1) 
            if cursor1.colliderect(boton3.rect):
                boton3.update(ventana, cursor1)
                if pg.mouse.get_pressed()[0]:
                    counter = 0
        # Si el contador es 0, se actualizará la imagen de fondo y los dos botones.
        if counter%2 == 0:
            ventana.blit(PinicioEscala, (0, 0))  
            boton1.update(ventana, cursor1)
            boton2.update(ventana, cursor1)
        cursor1.update()
        
        reloj1.tick(20)
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":  
    introduction() 