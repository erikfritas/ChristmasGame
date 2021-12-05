import pygame as pg
from pygame.locals import *
from Entities_.EntitiesBase_ import EntitiesBase_

class Player_(EntitiesBase_):
    def __init__(self, surface, name, rect, skin, keys={}, types={}):
        super().__init__(surface, name, rect, skin, types)

        self.keys = keys

    def draw(self):
        self.render()

    def update(self):
        for e in self.keys['move'].keys():
            if self.keys['move'][e]['is'] == True:
                if self.keys['move'][e]['pos'] == 'y' and self.keys['move'][e]['side'] != self.xy[1]:
                    self.rect[1] = self.keys['tomove'][e](self.rect[1], self.keys['speed'])
                elif self.keys['move'][e]['pos'] == 'x' and self.keys['move'][e]['side'] != self.xy[0]:
                    self.rect[0] = self.keys['tomove'][e](self.rect[0], self.keys['speed'])

    def keydown(self, e):
        if e.key in self.keys['move'].keys():
            self.keys['move'][e.key]['is'] = True

    def keyup(self, e):
        if e.key in self.keys['move'].keys():
            self.keys['move'][e.key]['is'] = False

    def keyevent(self, e):
        if e.type == KEYDOWN:
            self.keydown(e)
        
        if e.type == KEYUP:
            self.keyup(e)
