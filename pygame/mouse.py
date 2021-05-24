import pygame

# La clase cursor obtiene la posición del mouse en todo momento.
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1) 
        #El cursor se encontrara en la coordenada (0, 0) y sus lados seran de 1
    def update (self):
        self.left, self.top = pygame.mouse.get_pos() 
        #Mover el rectangulo invisible segun la posicion del mouse.