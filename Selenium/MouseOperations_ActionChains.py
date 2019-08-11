from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #to import special keys like tab, CapsLock,Shift,alt,pg up, enter etc.

path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver = Chrome(executable_path=path)
driver.get("http://www.thetestingworld.com")
driver.maximize_window()

act = ActionChains(driver)

#Click operation
#act.click()
#act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform() #This is by default left click

#Context click (Right Click)
#act.context_click().perform()
#act.context_click(driver.find_element_by_xpath("//a[text()='Login']").perform()

#Double Click
#act.double_click().perform()
#act.double_click(driver.find_element_by_xpath("//a[text()='Login']").perform()

#Hover
act.move_to_element(driver.find_element_by_xpath("//span[text() ='TUTORIAL ']")).perform()

#Drag&Drop
#act.drag_and_drop()
