'''
Created on Sep 6, 2015

@author: hugosenari
'''

from os.path import dirname
from inspect import getfile

def app_plugins_path():
    my_file = getfile(app_plugins_path)
    my_dir = dirname(my_file) 
    return my_dir 
