'''
Created on Sep 6, 2015

@author: hugosenari
'''

from circuits import Component, Event

class AMusicPlayer(Component):

    def started(self, component):
        print("Hi")
        
    def stopped(self, *args, **kwd):
        print("See ya!")
    
    def new_setup(self):
        print('Nice to meet you')
        
    def pause_track(self):
        print('I am a pause')
        
    def resume_track(self):
        print('I am a play')


class play_file(Event):
    """Evemt to play a file"""


class resume_track(Event):
    """Evemt to play current track"""


class stop_track(Event):
    """Evemt to stop current track"""


class pause_track(Event):
    """Evemt to pause current track"""


class played_track(Event):
    """Evemt when x time of current track are played"""


class go_to(Event):
    """Evemt go to x time of current track"""


class track_ended(Event):
    """Evemt when x time of curren file are played"""


class update(Event):
    """Evemt to update current track info"""
