import pygame as pg
from pygame.locals import *
from Windows_.BaseWindow_ import BaseWindow_
from modules import utils

# Fonts
fonte_size_default = 0
def fonte(name, size, bold=False, italic=False):
    return pg.font.SysFont(name, size+fonte_size_default, bold, italic)

text = lambda font, text, color=(255, 255, 255): font.render(text, True, color)


class ItemMenu_(BaseWindow_):
    def __init__(self, surface, SCREEN):
        self.SCREEN = SCREEN

        rects = {
            'window': [self.SCREEN["sw"]()*.5, self.SCREEN["sh"]()*.1, self.SCREEN["sw"]()*.4, self.SCREEN["sh"]()*.8],
            'ui': []
        }

        skins = {
            'window': (150, 150, 160),
            'ui': []
        }

        super().__init__(surface, rects, skins)

        self.infos = []
        self.info_pc = []

    def draw(self):
        super().draw()

        for i in self.infos:
            i()

        for i in self.info_pc:
            i()

    def set_info(self, info):
        if type(info) is dict:
            def column(i, gap=0):
                w = self.rects['window'][0] + int(self.rects['window'][2]/2) - int(i.get_width()/2)
                h = self.rects['window'][1] + 50 + gap
                return lambda: self.surface.blit(i, (w, h))

            self.infos = [
                column(text(fonte('Consolas', 35), info['title'])),
                column(text(fonte('Consolas', 18), info['description']), 50)
            ]

            def row(i, act, gap=0):
                w = self.rects['window'][0] + int(self.rects['window'][2]/2) + int(i.get_width()/2) - gap - 80
                h = self.rects['window'][1] + 150
                self.get_btn(i, w, h, act)
                return lambda: self.surface.blit(i, (w, h))

            self.info_pc = [
                row(text(fonte('Consolas', 22), f"SELL: +{info['sell']} $"), lambda: print(f"SELL: +{info['sell']} $"))
            ]
            if info['use']:
                self.info_pc.append(row(text(fonte('Consolas', 22), 'USE'), lambda: print('use'), 30))
        else:
            uis = self.render['ui'].copy()
            for i in uis:
                self.remove_ui(i)

    def get_btn(self, txt_obj, w, h, click_btn):
        id_ = utils.generate_random_id()
        rect_ = [
            w - 5,
            h - 5,
            txt_obj.get_width() + 10,
            txt_obj.get_height() + 10
        ]

        self.create_ui({
            id_: [
                rect_,
                (50, 50, 250),
                lambda s, r: pg.draw.rect(self.surface, s, r),
                click_btn,
                rect_.copy() # original position
            ]
        })
