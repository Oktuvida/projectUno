import pygame as pg

class Boton (pg.sprite.Sprite):
    def __init__(self, imagen1, imagen2, x, y, width=None,height=None, flip=None):
        self.imagen_normal = pg.image.load(imagen1)
        self.imagen_seleccionada = pg.image.load(imagen2)
        if width != None:
            self.imagen_normal = pg.transform.scale(self.imagen_normal, (width, height))
            self.imagen_seleccionada = pg.transform.scale(self.imagen_seleccionada, (width, height))
        if flip != None:
            self.imagen_normal = pg.transform.flip(self.imagen_normal, True, False)
            self.imagen_seleccionada = pg.transform.flip(self.imagen_seleccionada, True, False)
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        
        
    def update(self, pantalla, cursor, verify:bool=True):
        if cursor.colliderect(self.rect) and verify:
            self.imagen_actual = self.imagen_seleccionada
        else: 
            self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual, self.rect)

    def updatePosition(self, x, y):
        self.rect.left, self.rect.top = (x, y)
    
    def resize(self, width, height):
        self.imagen_normal = pg.transform.scale(self.imagen_normal, (width, height))
        self.imagen_seleccionada = pg.transform.scale(self.imagen_seleccionada, (width, height))