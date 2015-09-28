'''
Created on Sep 6, 2015

@author: hugosenari
'''

from circuits import Component, Event
from os import getenv, path, mkdir
import shelve


class Config(Component):
    """Configuration manager"""
    
    def init(self, appname):
        self._appname = appname
        self._shelf = None
        self._cfg_dir = None
        self._data_dir = None
        
    def started(self, component):
        self._set_cfg_dir()
        self._set_data_dir()

    def _set_cfg_dir(self):
        xdg_cfg = getenv("XDG_CONFIG_HOME", "~/.config")
        self._cfg_dir = path.sep.join([xdg_cfg, self._appname])
        
        if not path.isdir(self._cfg_dir):
            mkdir(self._cfg_dir)
            self.fire(new_setup())
        
        self.fire(cfg_dir(self._cfg_dir))
        
    def _set_data_dir(self):
        xdg_data = getenv("XDG_DATA_HOME", "~/.config")
        self._data_dir = path.sep.join([xdg_data, self._appname])

        if not path.isdir(self._data_dir):
            mkdir(self._data_dir)
        
        self.fire(data_dir(self._data_dir))
                
    def stopped(self, component):
        self.fire(config_stopping(self))
        if self._shelf:
            self._shelf.close()

    def cfg_dir(self, cfgdir):
        cfg_file = path.sep.join([cfgdir, self._appname])
        self._shelf = shelve.open(cfg_file)
        self.fire(config(self))

    def set_config(self, key, value):
        if self._shelf:
            self._shelf[key] = value
            self._shelf.sync()
        
    def get_confg(self, key):
        if self._shelf:
            return self._shelf[key]


class new_setup(Event):
    """New installation event"""


class set_config(Event):
    """Config change event"""


class config(Event):
    """Fired when config is ready"""


class config_stopping(Event):
    """Fired when config is stopping"""

    
class cfg_dir(Event):
    """Config dir found event"""

    
class data_dir(Event):
    """Data dir found event"""

