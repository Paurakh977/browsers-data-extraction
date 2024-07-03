import pygetwindow as gw
import time
from gugu import google_chr
while True:
    active_window = gw.getActiveWindow()
    if (active_window is not None) and  ("Google Chrome" in (active_window.title)):
            try:
                title=google_chr()
                print(title)
                time.sleep(3)
            except Exception as e:
                print("Errrorrr:",e)
    else:
        print("no chr")
        time.sleep(1)


            
