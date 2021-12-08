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

            for s_ui, r_ui in zip(self.skins["ui"], self.rects["ui"]):
                if type(s_ui) is tuple:
                    self.render["ui"][r_ui['id']] = [
                        pg.Rect(r_ui['rect']),
                        s_ui,
                        lambda s, r: pg.draw.rect(surface, s, r)
                    ]
                else:
                    self.render["ui"][r_ui['id']] = [
                        pg.Rect(r_ui['rect']),
                        pg.image.load(s_ui),
                        lambda s, r: surface.blit(s, (r[0], r[1]))
                    ]
        else:
            self.skins["window"] = pg.image.load(self.skins["window"])
            self.render["window"] = lambda: surface.blit(self.skins["window"], (self.rects["window"][0], self.rects["window"][1]))

        self.save_window = [self.render["window"], True]
        self.save_uis = self.render["ui"].copy()
        self.is_open = False

    def draw(self):
        self.render["window"]()
        for ui in self.render["ui"]:
            self.render["ui"][ui][2](self.render["ui"][ui][1], self.render["ui"][ui][0])

    def update(self):
        self.mouse_pos = pg.mouse.get_pos()
    
    def open_window(self):
        if not self.is_open and self.save_uis != {} and self.save_window[1]:
            self.is_open = True
            self.render["window"] = self.save_window[0]
            self.render["ui"] = self.save_uis
            self.save_window = [self.render["window"], False]
            self.save_uis = {}

    def close_window(self):
        if self.is_open and self.save_uis == {} and not self.save_window[1]:
            self.is_open = False
            self.save_window = [self.render["window"], True]
            self.save_uis = self.render["ui"]
            self.render["window"] = lambda: ''
            self.render["ui"] = {}

    def get_is_open(self):
        return self.is_open

    def create_ui(self, ui_skin, ui_rect):
        # (r, g, b) or "image_name.png"
        self.skins["ui"].append(ui_skin)

        # {'id': [pg.Rect([x, y, w, h]), skin, lambda s, r: pg.draw.rect(surface, s, r)]}
        # or
        # {'id': [pg.Rect([x, y, w, h]), skin, lambda s, r: surface.blit(s, (r[0], r[1]))]}
        self.rects["ui"].append(ui_rect)

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
