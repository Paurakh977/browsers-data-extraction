import time
import pygetwindow as gw
import funcs
import config

tab_name = "" 
used_time = 0
browser = ""

while True:
    title=None
    active_window = gw.getActiveWindow()
    
    if active_window is not None:
        if "Google Chrome" in active_window.title:
            browser = "Google Chrome"
            title=funcs.google_chr()
            used_time +=1
            time.sleep(1)
        elif "Microsoft​ Edge" in active_window.title:
            browser = "Microsoft Edge"
            title=funcs.get_edge_url()
            used_time +=1
            time.sleep(1)
            
        elif "Mozilla Firefox" in active_window.title:
            browser = "Mozilla Firefox"
            title=funcs.get_fire_fox()
            used_time +=1
            time.sleep(1)
            
        else:
            print("no browser active rn")
            time.sleep(1)
            
    if title :
        db = config
        db.insert(title,used_time,browser)
        print(title)
    
        