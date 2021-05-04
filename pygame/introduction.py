import pygame
from main import game


class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1) 
        #El cursor se encontrara en la coordenada (0, 0) y sus lados seran de 1
    def update (self):
        self.left, self.top = pygame.mouse.get_pos() 
        #Mover el rectangulo invisible segun la posicion del mouse.

    
class Boton (pygame.sprite.Sprite):
    def __init__(self, imagen1, imagen2, x, y):
        self.imagen_normal = imagen1
        self.imagen_seleccionada = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        
    def update(self, pantalla, cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccionada
        else: self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual, self.rect)
        
        
def introduction(): 
    pygame.init()           #Inicializamos módulo
    x = 800
    y = 600
    ventana = pygame.display.set_mode((x, y))   #Le damos un tamaño a la ventana
    pygame.display.set_caption("¡Uno!")  #Le damos un nombre a la ventana
    
    Pinicio = pygame.image.load("pygame/imgIntroduction/pantallaInicio.jpg")
    PinicioEscala = pygame.transform.scale(Pinicio, (x, y))
    jugar1 = pygame.image.load("pygame/imgIntroduction/jugar12.jpg")
    jugar2 = pygame.image.load("pygame/imgIntroduction/jugar22.jpg")
    instrucciones1 = pygame.image.load("pygame/imgIntroduction/instrucciones1.jpg")
    instrucciones2 = pygame.image.load("pygame/imgIntroduction/instrucciones2.jpg")
    #creditos1 = pygame.image.load("Creditos1.png")
    #creditos2 = pygame.image.load("Creditos2.png")
    
    
    reloj1 = pygame.time.Clock()
    boton1 = Boton(jugar1, jugar2, 250, 350)
    boton2 = Boton(instrucciones1, instrucciones2, 250, 450)
    #boton3 = Boton(creditos1, creditos2, 250, 550)
    cursor1 = Cursor()
    rojo = (200 , 0, 0)
    azul = (0, 0, 200)
    blanco = (255, 255, 255)
    colordefondo = blanco
    Game_over = False            #Loop infinito   
    while Game_over != True:   
              
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                        game()
                    if cursor1.colliderect(boton2.rect):
                        colordefondo = azul
            if event.type == pygame.QUIT:  
                Game_over = True

        reloj1.tick(20)
        ventana.blit(PinicioEscala, (0, 0))  
        cursor1.update()
        boton1.update(ventana, cursor1)
        boton2.update(ventana, cursor1)
        
        
        pygame.display.flip()
        
    #pygame.display.flip()
    pygame.quit()

introduction()
