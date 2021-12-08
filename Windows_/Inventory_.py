import pygame as pg
from pygame.locals import *
from Windows_.BaseWindow_ import BaseWindow_

class Inventory_(BaseWindow_):
    def __init__(self, surface, rects, skins):
        super().__init__(surface, rects, skins)

        self.bag_size = 8 # default bag_size
        self.bag = []

    def set_bag_size(self, slots):
        self.bag_size = slots

    def get_full_bag(self):
        return self.bag

    def update(self):
        pass
