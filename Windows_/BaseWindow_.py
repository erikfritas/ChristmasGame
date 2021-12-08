from os import lseek
import pygame as pg
from pygame.locals import *

class BaseWindow_:
    def __init__(self, surface, rects, skins):
        self.surface = surface
        self.rects = rects
        self.skins = skins
        self.render = {
            'window': lambda: None,
            'ui': {}
        }

        if type(skins["window"]) is tuple:
            self.render["window"] = lambda: pg.draw.rect(surface, self.skins["window"], self.rects["window"])

            for s_ui in self.skins["ui"]:
                if type(s_ui) is tuple:
                    for r_ui in self.rects["ui"]:
                        self.render["ui"][r_ui['id']] = lambda: pg.draw.rect(surface, s_ui, r_ui['rect'])
                else:
                    for r_ui in self.rects["ui"]:
                        self.render["ui"][r_ui['id']] = lambda: surface.blit(pg.image.load(s_ui), r_ui['rect'])

        else:
            self.skins["window"] = pg.image.load(self.skins["window"])
            self.render["window"] = lambda: surface.blit(self.skins["window"], (self.rects["window"][0], self.rects["window"][1]))

    def draw(self):
        self.render["window"]()
        for ui in self.render["ui"]:
            self.render["ui"][ui]

    def update(self):
        self.mouse_pos = pg.mouse.get_pos()
    
    def open_window(self):
        self.is_open = True
        
        self.render["window"] = self.save_window
        self.render["ui"] = self.save_uis

    def close_window(self):
        self.is_open = False

        self.save_window = self.render["window"]
        self.render["window"] = lambda: ''

        self.save_uis = self.render["ui"]
        self.render["ui"] = lambda: ''

    def get_is_open(self):
        return self.is_open

    def create_ui(self, ui_skin, ui_rect):
        self.skins["ui"].append(ui_skin) # (r, g, b) or "image_name.png"
        self.rects["ui"].append(ui_rect) # [x, y, w, h]

    def get_window_rect(self):
        return self.rects["window"]

    def get_ui_rect_by_id(self, id_):
        for ui in self.rects["ui"]:
            if ui["id"] == id_:
                return ui

    def on_click_window(self, action):
        if pg.Rect(self.rects["window"]).collidepoint(self.mouse_pos):
            action()
            print('window: colided with mouse')

    def on_click_ui(self, ui_id, action):
        if pg.Rect(self.get_ui_rect_by_id(ui_id)).collidepoint(self.mouse_pos):
            action()
            print('ui: colided with mouse')
