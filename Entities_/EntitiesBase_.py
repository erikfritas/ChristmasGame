import pygame as pg
from pygame.locals import *
from modules.utils import collidelist

class EntitiesBase_:
    def __init__(self, surface, name, rect, skin, types={}):
        self.name = name
        self.rect = rect
        self.skin = skin
        self.types = types
        self.surface = surface
        self.colliding = False
        self.xy = ["not", "not"]

        if type(self.skin) is tuple:
            self.render = lambda: pg.draw.rect(self.surface, self.skin, self.rect)
        else:
            img = pg.image.load(self.skin)
            self.render = lambda: self.surface.blit(img, (self.rect[0], self.rect[1]))
            pg.sprite.LayeredUpdates()

    def draw(self):
        self.render()

    def update(self):
        pass

    def set_collided(self, objs):
        for obj in objs:
            self.xy = obj.get_collided(pg.Rect(self.rect), self.xy)

            if self.xy != ["not", "not"]:
                break

    def set_collideds(self, objs):
        rects = []
        for obj in objs:
            rects.append(obj.get_rect())

        self.xy = collidelist(pg.Rect(self.rect), rects, self.xy)
