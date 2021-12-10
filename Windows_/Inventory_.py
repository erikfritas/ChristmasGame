import pygame as pg
from pygame.locals import *
from Windows_.BaseWindow_ import BaseWindow_
from modules import utils

class Inventory_(BaseWindow_):
    def __init__(self, surface):
        self.SCREEN = {
            "sw": lambda: surface.get_width(),
            "sh": lambda: surface.get_height()
        }

        rects = {
            'window': [self.SCREEN["sw"]()*.1, self.SCREEN["sh"]()*.1, self.SCREEN["sw"]()*.4, self.SCREEN["sh"]()*.8],
            'ui': []
        }

        skins = {
            'window': (100, 100, 110),
            'ui': []
        }

        super().__init__(surface, rects, skins)

        self.bag_size = [5, 4] # default bag_size [width, height]
        self.bag = []

        self.create_slots()
        self.set_bag_slots([
            {
                'id': utils.generate_random_id(),
                'item': 'Sword',
                'skin': (250, 50, 50)
            },
            {
                'id': utils.generate_random_id(),
                'item': 'Pickaxe',
                'skin': (250, 50, 50)
            }
        ])

    def draw(self):
        self.render["window"]()
        for ui in self.render["ui"]:
            self.render["ui"][ui][2](self.render["ui"][ui][1], self.render["ui"][ui][0])

    def set_bag_slots(self, slots):
        slot_i = 0
        for h_slot in range(0, self.bag_size[1]):
            for w_slot in range(0, self.bag_size[0]):
                slot_rect = pg.Rect([
                    (self.SCREEN["sw"]()*.1-50)+(100*(w_slot+1)),
                    (self.SCREEN["sh"]()*.1-50)+(100*(h_slot+1)), 50, 50])
                try:
                    self.bag[h_slot][w_slot] = slots[slot_i]['item']
                    self.create_ui({
                        slots[w_slot]['id']: [
                            slot_rect,
                            slots[w_slot]['skin'],
                            lambda s, r: pg.draw.rect(self.surface, s, r)
                        ]
                    })
                except:
                    self.bag[h_slot][w_slot] = []
                    self.create_ui({
                        utils.generate_random_id(): [
                            slot_rect,
                            (150, 50, 50),
                            lambda s, r: pg.draw.rect(self.surface, s, r)
                        ]
                    })
                
                slot_i += 1

        for b in self.bag:
            print(b)
        
        for ui in self.render["ui"].values():
            print(ui)
        print('\n\n',len(self.render['ui']))
        

    def get_full_bag(self):
        return self.bag

    def create_slots(self):
        for h_slot in range(0, self.bag_size[1]):
            self.bag.append([])
            for w_slot in range(0, self.bag_size[0]):
                self.bag[h_slot].append([])

    def update(self):
        pass
