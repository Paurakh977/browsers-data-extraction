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
mylist=list()
try:
    while True:
        active_window = gw.getActiveWindow()
        if active_window is not None:
            if "Google Chrome" in (active_window.title):
                title=google_chr()
                if (title not in mylist):
                    mylist.append(title)
                time.sleep(1)
except KeyboardInterrupt:
    print(mylist)
            
