'''
Created on Sep 6, 2015

@author: hugosenari
'''


#from circuits import Debugger
from .amusicplayer import AMusicPlayer 
from .config import Config
from .plugins_manager import PluginsManager

main = (
    AMusicPlayer() + 
    Config("AMusicPlayer") +
    PluginsManager({
        "simpl": {
            "module": "simpl",
            "active": True
        }
    })
    #+ Debugger()
)

if __name__ == '__main__':
    main.run()