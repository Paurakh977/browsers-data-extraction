import pygetwindow as gw
import time
from pywinauto import Application
from gugu import get_edge_url


try:
    while True:
        active_window = gw.getActiveWindow()
        if active_window is not None and "Microsoft​ Edge" in active_window.title:
            print(get_edge_url())
            

except KeyboardInterrupt:
    pass



