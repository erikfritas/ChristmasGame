import pygame as pg
from pygame.locals import *
from Entities_.EntitiesBase_ import EntitiesBase_
# TODO: from Windows_.Inventory_ import Inventory_

class Player_(EntitiesBase_):
    def __init__(self, surface, name, rect, skin, keys={}, types={}):
        super().__init__(surface, name, rect, skin, types)

        self.keys = keys

    def update(self):
        for e in self.keys['move'].keys():
            if self.keys['move'][e]['is'] == True:
                if self.keys['move'][e]['pos'] == 'y' and self.keys['move'][e]['side'] != self.xy[1]:
                    self.rect[1] = self.keys['tomove'][e](self.rect[1], self.keys['speed'])
                elif self.keys['move'][e]['pos'] == 'x' and self.keys['move'][e]['side'] != self.xy[0]:
                    self.rect[0] = self.keys['tomove'][e](self.rect[0], self.keys['speed'])

    def keyevent(self, e):
        if e.type == KEYDOWN:
            if e.key in self.keys['move'].keys():
                self.keys['move'][e.key]['is'] = True
        
        if e.type == KEYUP:
            if e.key in self.keys['move'].keys():
                self.keys['move'][e.key]['is'] = False
