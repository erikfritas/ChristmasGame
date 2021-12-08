import pygame as pg
from pygame.locals import *
from Entities_.EntitiesBase_ import EntitiesBase_
from Windows_.Inventory_ import Inventory_

class Player_(EntitiesBase_):
    def __init__(self, surface, name, rect, skin, types={}):
        windows = {
            'inventory': Inventory_(surface)
        }

        super().__init__(surface, name, rect, skin, types, windows)

        self.keys = {
            "move": {
                K_w: {'is': False, 'pos': 'y', 'side': 'top'},
                K_s: {'is': False, 'pos': 'y', 'side': 'bottom'},
                K_a: {'is': False, 'pos': 'x', 'side': 'left'},
                K_d: {'is': False, 'pos': 'x', 'side': 'right'}
            },
            "tomove": {
                K_w: lambda y, speed: y - speed,
                K_s: lambda y, speed: y + speed,
                K_a: lambda x, speed: x - speed,
                K_d: lambda x, speed: x + speed
            },
            "actions": {
                K_e: {
                    'is': False,
                    'act_down': lambda: self.handle_windows('inventory', True),
                    'act_up': lambda: self.handle_windows('inventory', False)
                }
            },
            "speed": 5
        }

        self.wait_for_click = False

    def update(self):
        for e in self.keys['move'].keys():
            if self.keys['move'][e]['is']:
                if self.keys['move'][e]['pos'] == 'y' and self.keys['move'][e]['side'] != self.xy[1]:
                    self.rect[1] = self.keys['tomove'][e](self.rect[1], self.keys['speed'])
                elif self.keys['move'][e]['pos'] == 'x' and self.keys['move'][e]['side'] != self.xy[0]:
                    self.rect[0] = self.keys['tomove'][e](self.rect[0], self.keys['speed'])

        for e in self.keys['actions'].keys():
            if self.keys['actions'][e]['is']:
                self.keys['actions'][e]['act_down']()
                self.wait_for_click = True
                #print('down')
            elif not self.keys['actions'][e]['is'] and self.wait_for_click:
                self.keys['actions'][e]['act_up']()
                self.wait_for_click = False
                #print('up')

        for name in self.windows.keys():
            if self.windows[name].get_is_open():
                self.windows[name].update()
        self.window_update()

    def keyevent(self, e):
        if e.type in [KEYDOWN, KEYUP]:
            if e.key in self.keys['move'].keys():
                self.keys['move'][e.key]['is'] = e.type == KEYDOWN
            if e.key in self.keys['actions'].keys():
                self.keys['actions'][e.key]['is'] = e.type == KEYDOWN
