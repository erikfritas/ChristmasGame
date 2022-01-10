import pygame as pg
from pygame.locals import *
from SpriteSheet_.SpriteBase_ import SpriteBase_
from modules.utils import *

clock = pg.time.Clock()

class SpritePlayer_(SpriteBase_):
    def __init__(self, surface, skin, rect, scale):
        super().__init__(surface, rect, scale)

        self.dir = skin[0][0]
        self.pos = skin[0][1]
        self.i = 0

    def animate(self, side):
        clock.tick(58)
        def a():
            self.i += 1
            try: self.pos[side][self.i]
            except: self.i = 0

        if clock.get_fps() >= 5: # loaded
            timer_per_second(.25, a, clock.get_fps())

        self.set_sheet(self.dir+self.pos[side][self.i])

        self.render()
