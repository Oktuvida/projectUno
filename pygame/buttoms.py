import pygame as pg

# La clase Boton inicializa un "objeto" que puede ser visto en la pantalla que genera Pygame.
class Boton (pg.sprite.Sprite):
    # Este requiere de cuatro parámetros: la path de una imagen, la path de este imagen siendo oprimida y la posición 
    # en el eje x y Y.
    # Como parámetros opcionales está su ancho y largo, como también si está invertida en el eje Y.
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
        
    # Este método hace visible el objeto antes inicializado en la pantalla. Requiere como parámetros una superficie 
    # como también otra clase llamada ¨cursor", que, como su nombre indica, posee todas las propiedades del puntero.
    # Como parámetro opcional está una variable booleana, la cual se encarga de hacer válida la interacción entre el 
    # cursor y el objeto. Esta "interacción" es equivalente a decir que la imagen está siendo pulsada.
    def update(self, pantalla, cursor, verify:bool=True):
        if cursor.colliderect(self.rect) and verify:
            self.imagen_actual = self.imagen_seleccionada
        else: 
            self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual, self.rect)

    # Actualiza la posición del objeto.
    def updatePosition(self, x, y):
        self.rect.left, self.rect.top = (x, y)
    
    # Actualiza el tamaño del objeto.
    def resize(self, width, height):
        self.imagen_normal = pg.transform.scale(self.imagen_normal, (width, height))
        self.imagen_seleccionada = pg.transform.scale(self.imagen_seleccionada, (width, height))