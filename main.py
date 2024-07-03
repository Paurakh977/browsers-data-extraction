import time
import pygetwindow as gw
import funcs
while True:
    title=None
    active_window = gw.getActiveWindow()
    if active_window is not None:
        if "Google Chrome" in active_window.title:
            title=funcs.google_chr()
            time.sleep(1)
        elif "Microsoft​ Edge" in active_window.title:
            title=funcs.get_edge_url()
            time.sleep(1)
            
        elif "Mozilla Firefox" in active_window.title:
            title=funcs.get_fire_fox()
            time.sleep(1)
            
        else:
            print("no browser active rn")
            time.sleep(1)
            
    if title:
        print(title)
    
        