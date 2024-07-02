# import pygetwindow as gw
# import time

# while True:
#     active_window = gw.getActiveWindow()
#     if active_window is not None:
#         print(active_window.title)
#     time.sleep(1) 

import pygetwindow as gw
import time
from gugu import google_chr
while True:
    active_window = gw.getActiveWindow()
    if (active_window is not None) and  ("Google Chrome" in (active_window.title)):
            try:
                title=google_chr()
                print(title)
                time.sleep(1)
            except Exception as e:
                print("Errrorrr:",e)
    else:
        print("no chr")
        time.sleep(1)


            
