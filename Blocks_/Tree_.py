import pygame as pg
from pygame.locals import *
from Blocks_.BlockBase_ import BlockBase_

class Tree_(BlockBase_):
    def __init__(self, surface, rect, skin, types={}):
        super().__init__(surface, rect, skin, types)

    def draw(self):
        self.render()
