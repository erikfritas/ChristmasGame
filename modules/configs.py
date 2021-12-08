import pygame as pg
from pygame.locals import *
import modules.utils as utils
from random import randint

from Entities_.Player_ import Player_
from Maps_.MapBase_ import MapBase_
from Blocks_.Tree_ import Tree_
from Windows_.Inventory_ import Inventory_

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
