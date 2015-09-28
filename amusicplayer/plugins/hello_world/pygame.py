'''
Created on Sep 6, 2015

@author: hugosenari
'''
from circuits import Component
from circuits import task

def show_window_pygame():
    from pygame.locals import QUIT
    from pygame import display, font, init, quit, event as blevent
    init()
    windowSurface = display.set_mode((400, 50))
    display.set_caption('Hello World PyGame')
    color = 255, 255, 255
    bg_color = 0, 0, 0
    text = font.SysFont(None, 48).render('Hello world PyGame', True, color, bg_color)
    textRect = text.get_rect()
    windowSurface.blit(text, textRect)
    display.update()
    while True:
        for event in blevent.get():
            if event.type == QUIT:
                quit()
                return 0


class HelloWorldPygame(Component):
    def hello_world(self, component):
        yield self.call(task(show_window_pygame))
