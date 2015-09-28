'''
Created on Sep 6, 2015

@author: hugosenari
'''
from circuits import Component
from circuits import task


def show_window_gtk():
    from gi.overrides.Gtk import Gtk
    class MyWindow(Gtk.Window):
    
        def __init__(self):
            super().__init__(title="Hello World Gtk")
    
            self.button = Gtk.Button(label="Hello World Gtk")
            self.add(self.button)
    win = MyWindow()
    def quit_gtk(*args, **kwd):
        Gtk.main_quit()
    win.connect("delete-event", quit_gtk)
    win.show_all()
    Gtk.main()


class HelloWorldGtk(Component):
    def hello_world(self, component):
        yield self.call(task(show_window_gtk))