from pywinauto import Application

while True:
    try:
        # Connect to Firefox window using title
        app = Application(backend='uia')
        app.connect(title_re=".*Mozilla Firefox.*", found_index=0)
        
        # Get the top-level Firefox window
        firefox_window = app.top_window()

        # Find the address bar control
        address_bar = firefox_window.child_window(control_type="Edit", found_index=0)
        
        # Get the URL from the address bar
        url = address_bar.get_value()
        
        print("Current URL:", url)
        
        # Wait or do some processing
        
    except Exception as e:
        print("Error occurred:", e)

