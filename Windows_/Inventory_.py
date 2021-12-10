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

    def set_bag_slots(self, slots):
        if len(slots) > self.bag_size[0] + self.bag_size[1]:
            raise Exception('slots\'re full -> set_bag_slots() error in Inventory_.py') # for python 3.8+

        slot_functs = [
            lambda: print('onclick: item'),
            lambda: print('onhold: item'),
            lambda: print('offclick: item (aparecerá o menu do item)'),
            lambda: print('ongrab: item (transforma a posição (x,y) desse rect na posição (x,y) do mouse)'),
            lambda: print('onholdgrab: item'),
            lambda: print('offgrab: item (troca os itens de lugar)'),

            lambda: print('onclick: empty'),
            lambda: print('onhold: empty'),
            lambda: print('offclick: empty'),
            lambda: print('ongrab: empty'),
            lambda: print('onholdgrab: empty'),
            lambda: print('offgrab: empty (troca a posição do item para essa posição que está vazia)')
        ]

        slot_i, slot_gap= 0, self.SCREEN["sw"]()*.0365
        for h_slot in range(0, self.bag_size[1]):
            for w_slot in range(0, self.bag_size[0]):
                slot_rect = pg.Rect([
                    (self.SCREEN["sw"]()*.1-slot_gap)+((slot_gap*2)*(w_slot+1)),
                    (self.SCREEN["sh"]()*.1-slot_gap)+((slot_gap*2)*(h_slot+1)), slot_gap, slot_gap])
                if len(slots) > slot_i:
                    self.bag[h_slot][w_slot] = slots[slot_i]['item']
                    self.create_ui({
                        slots[w_slot]['id']: [
                            slot_rect,
                            slots[w_slot]['skin'],
                            lambda s, r: pg.draw.rect(self.surface, s, r),
                            slot_functs[0], slot_functs[1], slot_functs[2],
                            slot_functs[3], slot_functs[4], slot_functs[5]
                        ]
                    })
                    slot_i += 1
                else:
                    self.bag[h_slot][w_slot] = []
                    self.create_ui({
                        utils.generate_random_id(): [
                            slot_rect,
                            (150, 50, 50),
                            lambda s, r: pg.draw.rect(self.surface, s, r),
                            slot_functs[6], slot_functs[7], slot_functs[8],
                            slot_functs[9], slot_functs[10], slot_functs[11]
                        ]
                    })

    def get_full_bag(self):
        return self.bag

    def create_slots(self):
        for h_slot in range(0, self.bag_size[1]):
            self.bag.append([])
            for w_slot in range(0, self.bag_size[0]):
                self.bag[h_slot].append([])

    def update(self):
        pass
