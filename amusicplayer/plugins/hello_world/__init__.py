'''
Created on Sep 6, 2015

@author: hugosenari
'''
from circuits.core.events import Event
from circuits.core.components import Component
from circuits.core.workers import Worker
from .pyglet_gui import HelloWorldPygletGui
from .pyglet import HelloWorldPyglet
from .pyside import HelloWorldPyside
from .pygame import HelloWorldPygame
from .pygtk import HelloWorldGtk

class HelloWorld(Component):
    """
    Hello World
    """
    def started(self, component):
#        Worker(process=True).register(self)
        HelloWorldPygletGui().register(self)
        HelloWorldPyglet().register(self)
        HelloWorldPyside().register(self)
        HelloWorldPygame().register(self)
        HelloWorldGtk().register(self)
        print("Hello World")
        self.fire(hello_world(self))

    def stopped(self, component):
        print("""Good Bye Cruel World""")


class hello_world(Event):
    """Hello World event"""


export = HelloWorld
name = "Example plugin"
description = """
My first plug-in that does nothing

Emits: hello_world
Handle: started, stopped
"""

if __name__ == '__main__':
    HelloWorld().run()