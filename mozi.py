from pywinauto import Application
import pygetwindow as gw
import time

# List of Top-Level Domains (TLDs)
tlds = [
    ".com", ".org", ".net", ".biz", ".info", ".name", ".pro", ".gov", ".edu", ".mil",
    ".us", ".uk", ".de", ".jp", ".cn", ".in", ".br", ".au", ".ca", ".mx", ".fr", ".it",
    ".nl", ".ru", ".np", ".co", ".io", ".ai", ".me", ".tv", ".xyz", ".jobs", ".travel",
    ".mobi", ".coop"
]

# Function to check and split the URL based on TLDs
def tld_checker(url):
    for tld in tlds:
        if tld in url:
            url = url.split(tld)[0]
            return url
    else:
        url = url.split('.')
        return max(url, key=len)

# Function to get the main name of the site from Firefox
def get_firefox_url():
    try:
        # Connect to the Firefox application
        app = Application(backend='uia').connect(title_re=".*Mozilla Firefox")
        window = app.window(title_re=".*Mozilla Firefox")

        # Locate the address bar element (adjust based on inspection results)
        url_bar = window.child_window(control_type="Edit", found_index=0)
        url = url_bar.get_value()

        # Clean and extract the main site name
        if "www." in url:
            url = url.split("www.")[-1]
        if "https://" in url:
            url = url.split('https://')[-1]
        if "http://" in url:
            url = url.split('http://')[-1]

        url = tld_checker(url)
        while "." in url:
            url = tld_checker(url)
        
        return url
    except Exception as e:
        print(f"Error getting Firefox URL: {e}")
        return None

# Function to continuously check for active Firefox window and print the main site name
def get_firefox_active_window_url():
    try:
        active_window = gw.getActiveWindow()
        if active_window is not None and "Mozilla Firefox" in active_window.title:
            return get_firefox_url()
        return None
    except Exception as e:
        print(f"Error getting Firefox URL: {e}")
        return None

try:
    while True:
        url = get_firefox_active_window_url()
        if url:
            print(url)
        time.sleep(1)  # Add a delay to reduce CPU usage
except KeyboardInterrupt:
    pass
