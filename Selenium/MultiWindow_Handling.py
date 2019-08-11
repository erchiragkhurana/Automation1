from selenium.webdriver import Chrome
path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get("http://www.naukri.com")

# 1.How to handle multiple window/popups
allwindow = driver.window_handles #It will give unique value assigned to different windows
# print(allwindow)
for win in allwindow:
    driver.switch_to.window(win)
    #print(driver.current_url)
    if (driver.current_url == "https://www.naukri.com/"):
        mainwin = win
        #print("This is my main window")
    else:
        driver.close()
driver.switch_to.window(mainwin)
print(driver.current_url) # It will throw NoSuchWindowException error as the window control was to the last window which we closed

