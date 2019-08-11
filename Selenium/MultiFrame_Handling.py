from selenium.webdriver import Chrome

path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get("https://www.toolsqa.com/iframe-practice-page/")
driver.switch_to.frame("IF1") #You can also use name as well
driver.find_element_by_xpath("//span[contains(text(),HOME)]").click()
driver.switch_to.default_content() #This will take out control from iframe to main window
driver.find_element_by_xpath("//span[text() ='VIDEOS']").click()

#driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='iframe2']"))
#driver.find_element_by_xpath("//a[contains(text(),Sortable)]").click()