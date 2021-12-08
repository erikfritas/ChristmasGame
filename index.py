from random import random
from modules.configs import *

# /var/www/html/python/jogos/ChristmasGame

class Game:
    def __init__(self):
        self.fps = text(fonte("Arial", 20), f'{int(clock.get_fps())}')

        self.objs = [
            [
                Player_(screen, "Player 1", [200, 200, 50, 50], skin=(255, 255, 255),
                types={
                    'collider': True
                })
            ], # players
            [
                Tree_(screen, [10, 10, 100, 100], (150, 50, 50), types={}),
                Tree_(screen, [400, 400, 100, 100], (150, 50, 50), types={}),
                Tree_(screen, [-30, 150, 100, 100], (150, 50, 50), types={})
            ], # blocks
            [], # npcs
            [], # enemies
            [], # hostile mobs
            [] # Windows
        ]

        self.entities = self.objs[0] + self.objs[3]

    def draw(self):
        screen.fill((0, 0, 10))
        self.fps = text(fonte("Arial", 20), f'{int(clock.get_fps())}')
        screen.blit(self.fps, (SCREEN["sw"]()-self.fps.get_width()-10, 10))

        for obj in self.objs:
            for o in obj:
                o.draw()

    def update(self):
        clock.tick(58)
        for e in pg.event.get():
            if e.type == QUIT:
                print('Game finished...')
                pg.quit()
                exit()

            for player in self.objs[0]:
                player.keyevent(e)

        for entity in self.entities:
            entity.set_collideds(self.objs[1])

        for update in self.objs:
            for el in update:
                el.update()

        # Timers
        #if clock.get_fps() >= 5: # loaded
            #utils.timer_per_second(1, lambda: print(clock.get_fps()), clock.get_fps())

    def loop(self):
        while True:
            self.update()
            self.draw()
            pg.display.update()

if __name__ == '__main__':
    Game().loop()
