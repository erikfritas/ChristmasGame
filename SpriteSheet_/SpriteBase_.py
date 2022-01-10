import pygame as pg
from pygame.locals import *

class SpriteBase_:
    def __init__(self, surface, rect, scale):
        self.surface = surface
        self.rect = rect
        self.scale = scale
        self.sheet = 0
    
    def set_sheet(self, sheet):
        self.sheet = pg.transform.scale(
            pg.image.load('./res/'+sheet), (int(2.25 * self.scale), 7 * self.scale)
        )

    def get_image(self):
        img = pg.Surface((self.rect[2], self.rect[3]))
        img.blit(self.sheet, (0, 0))
        img.set_colorkey((0, 0, 0))

        return img

    def render(self):
        self.surface.blit(self.get_image(), (self.rect[0], self.rect[1]))
