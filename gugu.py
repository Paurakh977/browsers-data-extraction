from pywinauto import Application

tlds = [
  # Generic Top-Level Domains (gTLDs)
  ".com",
  ".org",
  ".net",
  ".biz",
  ".info",
  ".name",
  ".pro",
  ".gov",
  ".edu",
  ".mil",
  # Country Code Top-Level Domains (ccTLDs)
  ".us",
  ".uk",
  ".de",
  ".jp",
  ".cn",
  ".in",
  ".br",
  ".au",
  ".ca",
  ".mx",
  ".fr",
  ".it",
  ".nl",
  ".ru",
  ".np",
  # Newer and Specialized TLDs
  ".co",
  ".io",
  ".ai",
  ".me",
  ".tv",
  ".xyz",
  # Others
  ".jobs",
  ".travel",
  ".mobi",
  ".coop"
]

def tld_checker(url):
    for tld in tlds:  
            if tld in url:
                url=url.split(tld)[0]
                return url
    else:
        url=url.split('.')
        return max(url,key=len)
                           
def google_chr():
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*", found_index=0)
    element_name="Address and search bar"
    dlg = app.top_window()
    try:
        url = dlg.child_window(title=element_name, control_type="Edit").get_value()
    except Exception as e:
        print(f"error in the module for chrome \n error is:\n{e}")
    try:
        if "www." in url:
            url=url.split("www.")[-1]
        if "https://" in url:
            url=url.split('https://')[-1]
                
    finally:
        url=tld_checker(url) 
        while "."in url:
            url=tld_checker(url)
        return url
                  
def get_edge_url():
        while True:
            app = Application(backend='uia')
            app.connect(title_re=".*Microsoft​ Edge.*", found_index=0)
            dlg = app.top_window()
            wrapper = dlg.child_window(title="App bar", control_type="ToolBar")
            try:
                url = wrapper.descendants(control_type='Edit')[0]
                url=url.get_value()
            except Exception as e:
                print(f"error in edge module \n{e}")
            try:
                if "www." in url:
                    url=url.split("www.")[-1]
                if "https://" in url:
                    url=url.split('https://')[-1]
            finally:
                url=tld_checker(url) 
                while "."in url:
                    url=tld_checker(url)
                return url
        
                
                    
        


            
        
    
      