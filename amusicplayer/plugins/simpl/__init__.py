'''
Created on Sep 6, 2015

@author: hugosenari
'''
from circuits.core.events import Event
from circuits.core.components import Component
from circuits.core.workers import Worker
from .pyglet_simplui import Simploop
from .player import SimplPlayer

class Simplui(Component):
    """
    Pyglet Simplui interface for amusicplayer
    """
    def started(self, component):
#        Worker(process=True).register(self)
        Simploop().register(self)
        SimplPlayer().register(self)

        self.fire(simplui_loaded(self))


class simplui_loaded(Event):
    """Hello World event"""


export = Simplui
name = "Simplui plugin"
description = """
My first interface

Emits: simplui_loaded
Handle: started
"""

if __name__ == '__main__':
    Simplui().run()