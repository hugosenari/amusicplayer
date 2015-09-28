'''
Created on Sep 6, 2015

@author: hugosenari
'''

from circuits.core.utils import safeimport
from circuits import Component, Event
from os import path
import sys

from .plugins import app_plugins_path

class PluginsManager(Component):
    """Plug-in load manager"""
    
    def init(self, my_plugin):
        self._plugins = {}
        self._init_plugins = my_plugin
        self._config = None
    
    def _add_dir_to_path(self, dir_path):
        if dir_path and path.isdir(dir_path):
            sys.path.insert(1, dir_path)
        return self
    
    def cfg_dir(self, loc):
        self._add_dir_to_path(
            app_plugins_path()
        )._add_dir_to_path(
            path.sep.join([loc, "plugins"])
        )

    def config_stopping(self, component):
        if self._config:
            self._config.set_config("plugins", self._plugins)
            self._shelf.close()
    
    def config(self, cfg):
        self.load_plugins(self._init_plugins)

        plugins_dict = cfg.get_confg("plugins")
        self.load_plugins(plugins_dict)

        self._config = cfg
        self.fire(plugins_manager(self))
        
    def load_plugins(self, plugins_dict):
        if plugins_dict:
            for plugin in plugins_dict.values():
                if  plugin and "module" in plugin and \
                    plugin["module"] not in self._plugins:
                    self.load_plugin(plugin)
        
    def load_plugin(self, plugin):
        """
        plugin: {
            "name": str,
            "module": str,
            "description": str,
            "active": False,
            "loaded": False,
            "failed": None,
            "export": None,
        }
        """
        new_plugin = {
            "name": plugin["module"],
            "description": plugin["module"],
            "active": False,
            "loaded": False,
            "failed": None,
            "export": None,
        }
        new_plugin.update(plugin)
        self._plugins[plugin["module"]] = new_plugin
        self._load_plugin_module(new_plugin)
        
    def _load_plugin_module(self, plugin):
        try:
            module = safeimport(plugin["module"])
            new_plugin = {
                "name": module.name,
                "description": module.description,
                "export": module.export,
                "loaded": True,
            }
            plugin.update(new_plugin)
        except Exception as e:
            plugin["failed"] = e
            print(e)

        if plugin["active"] and not plugin["failed"]:
            self.fire(active_plugin(plugin))
    
    def active_plugin(self, plugin):
        """Active plug-in handler"""
        if plugin and plugin["export"]:
            component = plugin["export"]()
            plugin["component"] = component 
            plugin["registry"] = component.register(self)
            plugin["registry"].started(component)
        
    def deactivate_plugin(self, plugin):
        """Deactivate plug-in handler"""
        if plugin["registry"]:
            plugin["registry"].unregister()
    
    def plugins(self):
        return self._plugins


class plugins(Event):
    """Event with"""


class plugins_manager(Event):
    """Event when plug-in manager is read"""


class load_plugin(Event):
    """Call me with pl ug-in to load"""


class active_plugin(Event):
    """Call me with plug-in do active"""


class deactivate_plugin(Event):
    """Call me with plug-in do deactivate"""
