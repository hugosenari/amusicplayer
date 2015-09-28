'''
Created on Sep 6, 2015

@author: hugosenari
'''
from circuits import Component
from circuits import task


def show_window_pyside():
    # Import PySide classes
    from PyQt5.Qt import QApplication, QLabel    
    # Create a Qt application
    app = QApplication([])
    # Create a Label and show it
    label = QLabel("Hello World Pyside")
    label.show()
    app.exec_()


class HelloWorldPyside(Component):
    def hello_world(self, component):
        yield self.call(task(show_window_pyside))
