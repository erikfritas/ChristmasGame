import pygame as pg
from pygame.locals import *
from modules.utils import *

class BlockBase_:
    def __init__(self, surface, rect, skin, types={}):
        self.surface = surface
        self.rect = rect
        self.skin = skin
        self.types = types

        if type(self.skin) is tuple:
            self.render = lambda: pg.draw.rect(self.surface, self.skin, self.rect)
        else:
            img = pg.image.load(self.skin)
            self.render = lambda: self.surface.blit(img, (self.rect[0], self.rect[1]))

    def draw(self):
        pass

    def update(self):
        pass

    def get_collided(self, obj, xy):
        rect = self.rect.copy()
        tolerance = 10
        rect[0] -= int(tolerance/2)
        rect[1] -= int(tolerance/2)
        rect[2] += tolerance
        rect[3] += tolerance
        return colliderect(obj, pg.Rect(rect), xy)

    def get_rect(self):
        rect = self.rect.copy()
        tolerance = 10
        rect[0] -= int(tolerance/2)
        rect[1] -= int(tolerance/2)
        rect[2] += tolerance
        rect[3] += tolerance
        return pg.Rect(rect)
