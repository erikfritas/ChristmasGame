import pygame as pg
from pygame.locals import *
from Entities_.Player_ import Player_
from Blocks_.Tree_ import Tree_
# import modules.utils as utils

clock = pg.time.Clock()

# WINDOW
WINDOW_SIZE = [800, 400]
screen = pg.display.set_mode(WINDOW_SIZE, RESIZABLE)

pg.init()

# Fonts
fonte_size_default = 0

def fonte(name, size, bold=False, italic=False):
    return pg.font.SysFont(name, size+fonte_size_default, bold, italic)

text = lambda font, text, color=(255, 255, 255): font.render(text, True, color)

SCREEN = {
    "sw": lambda: screen.get_width(),
    "sh": lambda: screen.get_height()
}
