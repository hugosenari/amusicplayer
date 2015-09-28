'''
Created on Sep 16, 2015

@author: hugosenari
'''

from pyglet.window import Window
from simplui.theme import pywidget_theme
from simplui.frame import Frame
from simplui.icons import LabelIcon,\
    PAUSE, PLAY_CIRCLE, CHEVRON_CIRCLE_RIGHT, CHEVRON_CIRCLE_LEFT, PLUS_CIRCLE
from simplui.layout import HLayout, VLayout
from circuits.core.components import Component
from circuits.core.events import Event
from amusicplayer.amusicplayer import pause_track, play_file, resume_track
from amusicplayer.playlist import play_next, play_prev, add_track


class SimplPlayer(Component):
    
    def simplui_loaded(self, component):
        self.component = component
        self._prev_ = LabelIcon(CHEVRON_CIRCLE_LEFT, action=self._prev)
        self._play_ = LabelIcon(PLAY_CIRCLE, action=self._play) 
        self._next_ = LabelIcon(CHEVRON_CIRCLE_RIGHT, action=self._next)
        self._add_  = LabelIcon(PLUS_CIRCLE, action=self._add)
        self._window_ = Window(200, 80, caption='AMusicPLayer')

        window = self._window_
        frame = Frame(
            pywidget_theme(),
            w=200, h=80,
            children=[
                VLayout(children=[
                    HLayout(children=[
                        self._prev_,
                        self._play_,
                        self._next_,
                        self._add_
                    ])
                ])
            ]
        )
        
        window.push_handlers(frame)
        
        @window.event
        def on_draw():
            window.clear()
            frame.draw()
            self.fire(main_window_draw(self, frame))
        
        
        @window.event
        def on_close():
            window.close()
            raise SystemExit()
        
    def _play(self, *args):
        if self._play_.text == PAUSE:
            self.fire(pause_track())
        else:
            self.fire(resume_track())
        
    def _next(self):
        self.fire(play_next())
        
    def _prev(self):
        self.fire(play_prev())
        
    def _add(self):
        self.fire(add_track())
        self.fire(play_file())
    
    def pause_track(self):
        self._play_.text = PLAY_CIRCLE
    
    def resume_track(self):
        self._play_.text = PAUSE


class main_window_close(Event):
    """The main window was closed"""

            
class main_window_draw(Event):
    """The main window was draws"""
