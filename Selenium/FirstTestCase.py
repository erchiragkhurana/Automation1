from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
#Step 1 is to open chrome browser
driver = Chrome(executable_path=path)

#Step 2 is to enter URL
driver.get("http://www.thetestingworld.com/testings")

#Step 3 is to maximize browser
driver.maximize_window()

#Step4 is to enter data into the text box
driver.find_element_by_name("fld_username").send_keys("helloworld")
driver.find_element_by_xpath("//input[@name ='fld_email']").send_keys("testingworldindia@gmail.com")
driver.find_element_by_xpath("//input[@name ='fld_password']").send_keys("abcd123")
driver.find_element_by_xpath("//input[@name ='fld_cpassword']").send_keys("abcd123")
#driver.find_element_by_name("fld_username").clear() - only if you want to clear something

#Step 5 - to work on drop-down, list (only by index, value & visible text)
obj = Select(driver.find_element_by_name("sex"))
#obj.select_by_index(1)
#obj.select_by_value("1") #it takes value as string so it should be in double quotes
obj.select_by_visible_text("Male")


#Step 6 is to click on radio button, checkbox, button & links
driver.find_element_by_xpath("//input[@value ='office']").click()
driver.find_element_by_name("terms").click()
#driver.find_element_by_xpath("//input[@type = 'submit']").click()
driver.find_element_by_link_text("Read Detail").click()
driver.find_element_by_class_name("close").click() # if you want to close it
#driver.close()

