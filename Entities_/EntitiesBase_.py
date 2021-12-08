import pygame as pg
from pygame.locals import *
from modules.utils import collidelist

class EntitiesBase_:
    def __init__(self, surface, name, rect, skin, types={}, windows=None):
        self.name = name
        self.rect = rect
        self.skin = skin
        self.types = types
        self.surface = surface
        self.colliding = False
        self.xy = ["not", "not"]

        if type(self.skin) is tuple:
            self.render = lambda: pg.draw.rect(self.surface, self.skin, self.rect)
        else:
            img = pg.image.load(self.skin)
            self.render = lambda: self.surface.blit(img, (self.rect[0], self.rect[1]))

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

    def set_collided(self, objs):
        for obj in objs:
            self.xy = obj.get_collided(pg.Rect(self.rect), self.xy)

            if self.xy != ["not", "not"]:
                break

    def set_collideds(self, objs):
        rects = []
        for obj in objs:
            rects.append(obj.get_rect())

        self.xy = collidelist(pg.Rect(self.rect), rects, self.xy)

    def open_window(self, name):
        if not self.windows[name].get_is_open():
            self.windows[name].open_window()
            print('open')

    def close_window(self, name):
        if self.windows[name].get_is_open():
            self.windows[name].close_window()
            print('close')

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

        
