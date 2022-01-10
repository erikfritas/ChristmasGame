import pygame as pg
from pygame.locals import *
from modules.utils import collidelist, timer_per_second

class EntitiesBase_:
    def __init__(self, surface, name, rect, skin, scale, spriteBase, types={}, windows=None):
        self.name = name
        self.rect = rect
        self.skin = skin
        self.scale = scale
        self.types = types
        self.surface = surface
        self.colliding = False
        self.xy = ["not", "not"]
        # [1 (doing), 'side' (side)]
        # ex: [1 (idle), 'right']
        self.status = 'right'

        if type(self.skin) is tuple:
            self.render = lambda: pg.draw.rect(self.surface, self.skin, self.rect)
        else:
            self.sprite = spriteBase(self.surface, self.skin, self.rect, self.scale)

            self.render = lambda: self.sprite.animate(self.status)

        self.windows = windows
        self.window_update = lambda: ''
        self.handled_window = False

    def draw(self):
        self.render()
        for name in self.windows.keys():
            if self.windows[name].get_is_open():
                self.windows[name].draw()

    def update(self):
        pass

    def set_collideds(self, objs):
        rects = []
        for obj in objs:
            rects.append(obj.get_rect())

        self.xy = collidelist(pg.Rect(self.rect), rects, self.xy)

    def open_window(self, name):
        if not self.windows[name].get_is_open():
            self.windows[name].open_window()
            #print('open')

    def close_window(self, name):
        if self.windows[name].get_is_open():
            self.windows[name].close_window()
            #print('close')

    def handle_windows(self, name, mousedown):
        if not mousedown and not self.handled_window:
            if not self.windows[name].get_is_open():
                self.window_update = lambda: self.open_window(name)
                #print('opened')
            else:
                self.window_update = lambda: self.close_window(name)
                #print('closed')
        else:
            self.handled_window = False

        
