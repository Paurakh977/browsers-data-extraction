import pygetwindow as gw
import time
from pywinauto import Application
from gugu import get_edge_url
try:
    while True:
        active_window = gw.getActiveWindow()
        if active_window is not None and "Microsoft​ Edge" in active_window.title:
            try:
                print(get_edge_url())
            except Exception as e:
                print(f'THE ERROR is:{e}')                
        else:
            time.sleep(1)
            print(active_window.title)
            
except KeyboardInterrupt:   
    pass



