'''
Created on Sep 6, 2015

@author: hugosenari
'''
from circuits import Component

from circuits.core.events import Event
from circuits.core.values import Value

from pyglet.app.base import EventLoop
from pyglet.app import platform_event_loop

class MyEventLoop(EventLoop):
    def run(self):
        '''Begin processing events, scheduled functions and window updates.

        This method returns when `has_exit` is set to True.

        Developers are discouraged from overriding this method, as the
        implementation is platform-specific.
        '''
        self.has_exit = False
        self._legacy_setup()

        platform_event_loop.start()
        self.dispatch_event('on_enter')

        self.is_running = True
        while not self.has_exit:
            self.idle()
            platform_event_loop.step(None)
            yield None
        self.is_running = False
            
        self.dispatch_event('on_exit')
        platform_event_loop.stop()
        yield 0


class Simploop(Component):
    def simplui_loaded(self, component):
        if MyEventLoop:
            event = pyglet_tick()
            event.value = Value()
            self.registerTask(
                (
                    event,
                    MyEventLoop().run()
                )
            )


class pyglet_tick(Event):
    """Pyglet tick event"""
