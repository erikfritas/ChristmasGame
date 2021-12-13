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
                        lambda s, r: pg.draw.rect(surface, s, r),
                        lambda: print('onclick: item'),
                        lambda: print('onhold: item'),
                        lambda: print('offclick: item')
                    ]
                else:
                    self.render["ui"][r_ui['id']] = [
                        pg.Rect(r_ui['rect']),
                        pg.image.load(s_ui),
                        lambda s, r: surface.blit(s, (r[0], r[1])),
                        lambda: print('onclick: item'),
                        lambda: print('onhold: item'),
                        lambda: print('offclick: item')
                    ]
        else:
            self.skins["window"] = pg.image.load(self.skins["window"])
            self.render["window"] = lambda: surface.blit(self.skins["window"], (self.rects["window"][0], self.rects["window"][1]))

        self.save_window = [self.render["window"], True]
        self.save_uis = self.render["ui"].copy()
        self.is_open = False
        self.border = lambda: ''
        self.border_color = None

    def draw(self):
        if self.border_color == None:
            self.border_hover = lambda a, b, c, d: ''

        self.render["window"]()
        for ui in self.render["ui"]:
            self.render["ui"][ui][2](self.render["ui"][ui][1], self.render["ui"][ui][0])
            self.border_hover(ui, self.border_color, self.render["ui"][ui][0], 5)
        self.border()
    
    def draw_border(self, color, rect, border_size):
        self.border = lambda: pg.draw.rect(self.surface, color, rect, border_size)

    def update(self):
        pass
    
    def open_window(self):
        self.is_open = True
        self.render["window"] = self.save_window[0]
        self.render["ui"] = self.save_uis
        self.save_window = [self.render["window"], False]
        self.save_uis = {}

    def close_window(self):
        self.is_open = False
        self.save_window = [self.render["window"], True]
        self.save_uis = self.render["ui"]
        self.render["window"] = lambda: ''
        self.render["ui"] = {}

    def get_is_open(self):
        return self.is_open

    def create_ui(self, ui):
        # {'id': [pg.Rect([x, y, w, h]), skin=(r, g, b) or "image_name.png", lambda s, r: pg.draw.rect(surface, s, r)]}
        # or
        # {'id': [pg.Rect([x, y, w, h]), skin, lambda s, r: surface.blit(s, (r[0], r[1]))]}

        for u in ui:
            self.render["ui"][u] = ui[u]
            self.save_uis = self.render["ui"].copy()

    def remove_ui(self, ui_id):
        self.render["ui"].pop(ui_id)
        self.save_uis = self.render["ui"].copy()

    def get_window_rect(self):
        return self.rects["window"]

    def get_ui_rect_by_id(self, id_):
        for ui_id in self.render["ui"]:
            if ui_id == id_:
                return self.render["ui"][ui_id][0]

        raise Exception(f"This id_ ({id_}) not exists in uis")

    # CLICK, HOLD or OFF
    def ohf_click(self, on_, limit=2):
        for ui_id in self.render["ui"]:
            self.on_hover_ui(ui_id, self.render["ui"][ui_id][on_+limit])

    def on_hover_window(self, action):
        if pg.Rect(self.render["window"]).collidepoint(pg.mouse.get_pos()):
            action()

    def on_hover_ui(self, ui_id, action):
        if pg.Rect(self.get_ui_rect_by_id(ui_id)).collidepoint(pg.mouse.get_pos()):
            action()
    
    def border_hover(self, ui_id, color, rect, bd_size):
        self.on_hover_ui(ui_id, lambda: self.draw_border(color, rect, bd_size))
