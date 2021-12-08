import pygame as pg
from pygame.locals import *
from modules.utils import *

class MapBase_:
    def __init__(self, surface, mapsize, skintiles, types={}):
        self.surface = surface
        self.mapsize = mapsize
        self.skintiles = skintiles
        self.types = types
        self.rend = 0
        self.fullmap = []
        self.map = []

        if type(self.skintiles) is tuple:
            self.render = lambda: pg.draw.rect(self.surface, self.skin, self.rect)
        else:
            self.rend = []
            for skin in self.skintiles:
                img = pg.image.load(skin)
                self.rend.append(lambda: self.surface.blit(img, (self.rect[0], self.rect[1])))

        if type(self.rend) is list:
            def render_img():
                for r in self.rend:
                    r()
            self.render = render_img

    def generate_full_map(self, block=50):
        self.fullmap = []

        for w in range(0, self.mapsize[0], block):
            for h in range(0, self.mapsize[1], block):
                self.map.append()
