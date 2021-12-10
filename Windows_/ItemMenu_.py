import pygame as pg
from pygame.locals import *
from Windows_.BaseWindow_ import BaseWindow_
from modules import utils

# Fonts
fonte_size_default = 0
def fonte(name, size, bold=False, italic=False):
    return pg.font.SysFont(name, size+fonte_size_default, bold, italic)

text = lambda font, text, color=(255, 255, 255): font.render(text, True, color)


class ItemMenu_(BaseWindow_):
    def __init__(self, surface, SCREEN):
        self.SCREEN = SCREEN

        rects = {
            'window': [self.SCREEN["sw"]()*.5, self.SCREEN["sh"]()*.1, self.SCREEN["sw"]()*.4, self.SCREEN["sh"]()*.8],
            'ui': []
        }

        skins = {
            'window': (150, 150, 160),
            'ui': []
        }

        super().__init__(surface, rects, skins)

    def draw(self, item_information):
        super().draw()
        info = text(fonte('Consolas', 20), item_information)
        self.surface.blit(info, (self.rects['window'][0], self.rects['window'][1]))
