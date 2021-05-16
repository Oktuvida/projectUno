import pygame
from main import game
from time import sleep
from os import environ
from buttoms import Boton
from mouse import Cursor

        
        
def introduction(): 
    environ["SDL_VIDEO_WINDOW_POS"] = "0, 0"
    pygame.init()           #Inicializamos módulo
    x = 960
    y = 640
    ventana = pygame.display.set_mode((x, y))   #Le damos un tamaño a la ventana
    pygame.display.set_caption("¡Uno!")  #Le damos un nombre a la ventana
    
    Pinicio = pygame.image.load("pygame/imgIntroduction/pantallaInicio.jpg")
    PinicioEscala = pygame.transform.scale(Pinicio, (x, y))
    jugar1 = pygame.image.load("pygame/imgIntroduction/jugar12.jpg")
    jugar2 = pygame.image.load("pygame/imgIntroduction/jugar22.jpg")
    instrucciones1 = pygame.image.load("pygame/imgIntroduction/instrucciones1.jpg")
    instrucciones2 = pygame.image.load("pygame/imgIntroduction/instrucciones2.jpg")
    fondInstruc = pygame.transform.scale(pygame.image.load("./esthetic/Instrucciones.png"), (x, y))
    lArrow = pygame.transform.flip(pygame.transform.scale(pygame.image.load("./esthetic/Fde.png"), (50, 50)), True, False)
    lArrowOp = pygame.transform.scale(pygame.image.load("./esthetic/Fizop.png"), (50, 50))
    counter = 0


    reloj1 = pygame.time.Clock()

    boton1 = Boton(jugar1, jugar2, x//2-125, y//2+25)
    boton2 = Boton(instrucciones1, instrucciones2, x//2-125, y//2+125)

    cursor1 = Cursor()

    Game_over = False            #Loop infinito   
    while Game_over != True:   
              
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                        game()
                    if cursor1.colliderect(boton2.rect):
                        ventana.blit(fondInstruc, (0, 0))
                        seeArrow = ventana.blit(lArrow, (75, 50))
                        counter = 1
                        
            if event.type == pygame.QUIT:  
                Game_over = True
        if counter%2!=0:
            seeArrow = ventana.blit(lArrow, (75, 50)) 
            if cursor1.colliderect(seeArrow):
                seeArrow = ventana.blit(lArrowOp, (75, 50))
                if pygame.mouse.get_pressed()[0]:
                    counter = 0
        if counter%2 == 0:
            ventana.blit(PinicioEscala, (0, 0))  
            boton1.update(ventana, cursor1)
            boton2.update(ventana, cursor1)
        cursor1.update()
        
        reloj1.tick(20)
        pygame.display.flip()

    #pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":  
    introduction()