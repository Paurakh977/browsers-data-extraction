import pygetwindow as gw
import time
from gugu import get_fire_fox
while True:
    active_window = gw.getActiveWindow()
    if (active_window is not None) and  ("Mozilla Firefox" in (active_window.title)):
            try:
                title=get_fire_fox()
                print(title)
                time.sleep(3)
            except Exception as e:
                print("Errrorrr:",e)
    else:
        print("no fox")
        time.sleep(1)


            
