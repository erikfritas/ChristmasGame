import pygame as pg
from pygame.locals import *
from Windows_.BaseWindow_ import BaseWindow_
from Windows_.ItemMenu_ import ItemMenu_
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
                'item': {
                    'title': 'Wood Sword',
                    'description': 'Uma espada de madeira, bem fácil de fazer :)',
                    'pros': [
                        'ATTACK POWER: 3',
                        'BREAK POWER: 1'
                    ],
                    'contras': [
                        'DEFENSE: -1',
                        'ATTACK SPEED: 1'
                    ],
                    'use': True,
                    'using': True,
                    'sell': 3
                },
                'skin': (250, 50, 50)
            },
            {
                'id': utils.generate_random_id(),
                'item': {
                    'title': 'Wood Pickaxe',
                    'description': 'Uma picareta de madeira, bem fácil de fazer :)',
                    'pros': [
                        'ATTACK POWER: 1',
                        'BREAK POWER: 3'
                    ],
                    'contras': [
                        'DEFENSE: -1',
                        'ATTACK SPEED: 1'
                    ],
                    'use': True,
                    'using': False,
                    'sell': 4
                },
                'skin': (250, 50, 50)
            }
        ])
        self.item_info = 'item'
        self.ItemMenu = ItemMenu_(surface, self.SCREEN)
        self.render_menu = lambda: ''
        self.grabing_rect = ''
        self.border_color = (20, 20, 25)

    def draw(self):
        super().draw()
        self.render_menu()

    def update(self):
        pass

    def get_itemMenu(self):
        return self.ItemMenu

    def set_bag_slots(self, slots):
        if len(slots) > self.bag_size[0] + self.bag_size[1]:
            raise Exception('slots\'re full -> set_bag_slots() error in Inventory_.py') # for python 3.8+

        def set_menu(i):
            self.ItemMenu.set_info('')
            if type(i) is not str:
                self.ItemMenu.set_info(i['item'])
                self.render_menu = lambda: self.ItemMenu.draw()
            else:
                self.render_menu = lambda: ''
            if type(self.grabing_rect) is not str:
                self.render['ui'][i['id']][0] = self.render['ui'][i['id']][-1].copy()
                self.grabing_rect = ''

        def set_grabing(i):
            self.grabing_rect = [self.render['ui'][i['id']][-1].copy(), i['id']]
            width = int(self.grabing_rect[0][2]/2)
            height = int(self.grabing_rect[0][3]/2)
            self.render['ui'][i['id']][0][0] = pg.mouse.get_pos()[0]-width
            self.render['ui'][i['id']][0][1] = pg.mouse.get_pos()[1]-height
            self.render_menu = lambda: set_grabing(i)

        def change_grab(id_):
            if type(self.grabing_rect) is list and self.render['ui'][self.grabing_rect[1]].copy() != self.grabing_rect[0].copy():
                self.render['ui'][self.grabing_rect[1]][0] = self.render['ui'][id_][-1].copy()
                self.render['ui'][self.grabing_rect[1]][-1] = self.render['ui'][id_][-1].copy()
                self.render['ui'][id_][0] = self.grabing_rect[0].copy()
                self.render['ui'][id_][-1] = self.grabing_rect[0].copy()
                self.grabing_rect = ''

        slot_functs = [
            lambda i: lambda: '', # onclick: item
            lambda i: lambda: '', # onhold: item,
            lambda i: lambda: set_menu(i[0]), # offclick: item (menu do item aparece) e (volta os itens ao seus lugares)
            lambda i: lambda: '', # ongrab: item,
            lambda i: lambda: set_grabing(i[0]), # onholdgrab: item (a posição (x,y) desse rect = (x,y) do mouse)
            lambda i: lambda: '', # offgrab: item

            lambda i: lambda: change_grab(i), # onclick: empty (troca a posição do item para essa posição)
            lambda i: lambda: '', # onhold: empty,
            lambda i: lambda: set_menu(i), # offclick: empty (menu desaparece)
            lambda i: lambda: '', # ongrab: empty,
            lambda i: lambda: '', # onholdgrab: empty,
            lambda i: lambda: '' # offgrab: empty
        ]

        slot_i, slot_gap= 0, self.SCREEN["sw"]()*.0365
        for h_slot in range(0, self.bag_size[1]):
            for w_slot in range(0, self.bag_size[0]):
                slot_rect = pg.Rect([
                    (self.SCREEN["sw"]()*.1-slot_gap)+((slot_gap*2)*(w_slot+1)),
                    (self.SCREEN["sh"]()*.1-slot_gap)+((slot_gap*2)*(h_slot+1)), slot_gap, slot_gap])
                if len(slots) > slot_i:
                    name = [slots[slot_i], slot_rect]
                    self.bag[h_slot][w_slot] = name[0]['item']
                    self.create_ui({
                        slots[w_slot]['id']: [
                            slot_rect,
                            slots[w_slot]['skin'],
                            lambda s, r: pg.draw.rect(self.surface, s, r),
                            slot_functs[0](name), slot_functs[1](name), slot_functs[2](name),
                            slot_functs[3](name), slot_functs[4](name), slot_functs[5](name),
                            slot_rect.copy() # original position
                        ]
                    })
                    slot_i += 1
                else:
                    self.bag[h_slot][w_slot] = []
                    name = utils.generate_random_id()
                    self.create_ui({
                        name: [
                            slot_rect,
                            (150, 50, 50),
                            lambda s, r: pg.draw.rect(self.surface, s, r),
                            slot_functs[6](name), slot_functs[7](name), slot_functs[8](name),
                            slot_functs[9](name), slot_functs[10](name), slot_functs[11](name),
                            slot_rect.copy() # original position
                        ]
                    })

    def get_full_bag(self):
        return self.bag

    def create_slots(self):
        for h_slot in range(0, self.bag_size[1]):
            self.bag.append([])
            for w_slot in range(0, self.bag_size[0]):
                self.bag[h_slot].append([])
