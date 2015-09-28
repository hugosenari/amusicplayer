'''
Created on Sep 6, 2015

@author: hugosenari
'''
from circuits import Component
from circuits import task


def show_window_pyglet():
    import pyglet
    window = pyglet.window.Window(width=500, height=100, caption="Hello World")
    label = pyglet.text.Label('Hello, world Pyglet', font_size=36,
        x=window.width//2, y=window.height//2,anchor_x='center',
        anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        label.draw()
    pyglet.app.run()
    return 0


class HelloWorldPyglet(Component):
    def hello_world(self, component):
        yield self.call(task(show_window_pyglet))

    def tick(self, *args, **kwd):
        print('tick')