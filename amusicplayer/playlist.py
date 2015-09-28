'''
Created on Sep 6, 2015

@author: hugosenari
'''

from circuits import Component, Event
from os.path import sep
import shelve

class Playlist(Component):
    """Playlist componet"""
    
    def init(self):
        self._shelf = None
        self._size = 0
        self._current = None
        self._list = []
    
    def data_dir(self, datadir):
        pls_file = sep.join([datadir,  "playlist"])
        self._shelf = shelve.open(pls_file)


class play_next(Event):
    """Evemt to play next track"""


class play_prev(Event):
    """Evemt to play previous track"""


class add_track(Event):
    """Evemt to add track to the end"""


class add_as_next(Event):
    """Evemt to add track as next"""

class list_tracks(Event):
    """Evemt to list tracks"""

class empty_tracks(Event):
    """Evemt to list tracks"""

