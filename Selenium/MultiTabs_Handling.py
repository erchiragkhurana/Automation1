from selenium.webdriver import Chrome

path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get("https://www.thetestingworld.com/testings")
driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Delete')]").click()

alltabs = driver.window_handles #It will give unique value

for tab in alltabs:
    driver.switch_to.window(tab)
    #print(driver.current_url)
    if (driver.current_url == "https://www.thetestingworld.com/testings/manage_customer.php"): #You can also use title or any unique element
        driver.find_element_by_xpath("//button[text()='Start Download']").click()
