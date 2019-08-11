from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #to import special keys like tab, CapsLock,Shift,alt,pg up, enter etc.

path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)

driver.get("http://www.thetestingworld.com/testings")
driver.maximize_window()

driver.find_element_by_name("fld_username").send_keys("Hello")

act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() #when you to use special keys then you need to use Keys class with upper otherwise small double quotes
#act.send_keys(Keys.TAB).perform()