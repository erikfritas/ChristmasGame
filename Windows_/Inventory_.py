import pygame as pg
from pygame.locals import *
from Windows_.BaseWindow_ import BaseWindow_
from modules import utils

class Inventory_(BaseWindow_):
    def __init__(self, surface):
        SCREEN = {
            "sw": lambda: surface.get_width(),
            "sh": lambda: surface.get_height()
        }

        rects = {
            'window': [SCREEN["sw"]()*.25, SCREEN["sh"]()*.25, SCREEN["sw"]()*.5, SCREEN["sh"]()*.5],
            'ui': [
                {
                    'id': utils.generate_random_id(),
                    'rect': [250, 250, 50, 50]
                },
                {
                    'id': utils.generate_random_id(),
                    'rect': [325, 250, 50, 50]
                }
            ]
        }
        
        skins = {
            'window': (100, 100, 110),
            'ui': [
                (50, 100, 150),
                (50, 100, 150)
            ]
        }

        super().__init__(surface, rects, skins)

        self.bag_size = 8 # default bag_size
        self.bag = []

    def set_bag_size(self, slots):
        self.bag_size = slots

    def get_full_bag(self):
        return self.bag

    def update(self):
        pass
