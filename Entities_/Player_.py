import pygame as pg
from pygame.locals import *
from Entities_.EntitiesBase_ import EntitiesBase_
from Windows_.Inventory_ import Inventory_

class Player_(EntitiesBase_):
    def __init__(self, surface, name, rect, skin, scale, spriteBase, types={}):
        windows = {
            'inventory': Inventory_(surface)
        }

        super().__init__(surface, name, rect, skin, scale, spriteBase, types, windows)

        self.keys = {
            "move": {
                K_w: {'is': False, 'pos': 1, 'side': 'top'},
                K_s: {'is': False, 'pos': 1, 'side': 'bottom'},
                K_a: {'is': False, 'pos': 0, 'side': 'left'},
                K_d: {'is': False, 'pos': 0, 'side': 'right'}
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
            "mouse": {
                1: {
                    'is': False,
                    'act_down': lambda: self.click_acts([
                        lambda: self.windows['inventory'].ohf_click(1)
                    ]), # onclick
                    'act_hold': lambda: '', #self.windows['inventory'].ohf_click(2), # onhold
                    'act_up': lambda: self.click_acts([
                        lambda: self.windows['inventory'].ohf_click(3),
                        lambda: self.windows['inventory'].get_itemMenu().ohf_click(1)
                    ]) # offclick
                },
                3: {
                    'is': False,
                    'act_down': lambda: self.click_acts([
                        lambda: self.windows['inventory'].ohf_click(4)
                    ]), # ongrab
                    'act_hold': lambda: self.click_acts([
                        lambda: self.windows['inventory'].ohf_click(5)
                    ]), # onholdgrab
                    'act_up': lambda: self.click_acts([
                        lambda: self.windows['inventory'].ohf_click(6)
                    ]) # offgrab
                }
            },
            "speed": 5
        }

        self.wait_for_click = ['key', False]
        self.wait_for_m_click = ['key', False]

    def click_acts(self, acts):
        for act in acts:
            act()

    def update(self):
        self.status = 'idle'
        for e in self.keys['move'].keys():
            if self.keys['move'][e]['is']:
                pos = self.keys['move'][e]['pos']
                if self.keys['move'][e]['side'] != self.xy[pos]:
                    self.rect[pos] = self.keys['tomove'][e](self.rect[pos], self.keys['speed'])
                    self.status = self.keys['move'][e]['side']

        for e in self.keys['actions'].keys():
            if self.keys['actions'][e]['is']:
                self.keys['actions'][e]['act_down']()
                self.wait_for_click = [e, True]
            elif e == self.wait_for_click[0] and self.wait_for_click[1]:
                self.keys['actions'][e]['act_up']()
                self.wait_for_click = [e, False]
        
        for e in self.keys['mouse'].keys():
            if self.keys['mouse'][e]['is']:
                if not self.wait_for_m_click[1]:
                    self.keys['mouse'][e]['act_down']()
                    self.wait_for_m_click = [e, True]
                elif e == self.wait_for_m_click[0]:
                    self.keys['mouse'][e]['act_hold']()
            elif e == self.wait_for_m_click[0] and self.wait_for_m_click[1]:
                self.keys['mouse'][e]['act_up']()
                self.wait_for_m_click = [e, False]

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
        
        if e.type in [MOUSEBUTTONDOWN, MOUSEBUTTONUP]:
            if e.button in self.keys['mouse'].keys():
                self.keys['mouse'][e.button]['is'] = e.type == MOUSEBUTTONDOWN
