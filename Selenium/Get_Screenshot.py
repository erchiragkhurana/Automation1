from selenium.webdriver import Chrome

path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get("http://www.thetestingworld.com/testings")
driver.get_screenshot_as_file("C:/Users/chirag/PycharmProjects/Automation1/Selenium/Screenshot1.png")

#Second method is to create a method for screenshots
def take_page_screenshot(driver, name):
    driver.get_screenshot_as_file("C:/Users/chirag/PycharmProjects/Automation1/Selenium/" + name + ".png")

#wherever we want to call the above method, this is called taking screenshot at runtime
# 1.we import this module at the top
# 2. Then Get_Screenshot.take_page_screenshot(driver, "First_Screenshot")