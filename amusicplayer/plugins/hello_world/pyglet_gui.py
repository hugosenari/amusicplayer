'''
Created on Sep 6, 2015

@author: hugosenari
'''
from circuits import Component

from circuits.core.events import Event
from circuits.core.values import Value

try:
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
            yield from self._run_estimated()
            self.is_running = False
                
            self.dispatch_event('on_exit')
            platform_event_loop.stop()
    
    
        def _run_estimated(self):
            '''Run-loop that continually estimates function mapping requested
            timeout to measured timeout using a least-squares linear regression.
            Suitable for oddball platforms (Windows).
            '''
            
            while not self.has_exit:
                self.idle()
                platform_event_loop.step(None)
                yield None
            yield 0

except:
    MyEventLoop = None


def show_window_pyglet_gui():
    from pyglet.window import Window
    from simplui.theme import PyWidget
    from simplui.frame import Frame
    from simplui.label import Label       
    window = Window(200, 50, caption='Hello Window')
    frame = Frame(
        PyWidget,
        children=[
            Label('Hello World', x=18, y=25)
        ]
    )
    
    @window.event
    def on_draw():
        window.clear()
        frame.draw()
    
    
    @window.event
    def on_close():
        window.close()


class HelloWorldPygletGui(Component):
    def hello_world(self, component):
        if MyEventLoop:
            show_window_pyglet_gui();
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
