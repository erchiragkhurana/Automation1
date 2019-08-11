from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time

import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
    # open chrome browser
    driver = Chrome(executable_path=path)
    #driver.set_page_load_timeout(10) #by default is 30 seconds in selenium and it wil be before URL, if it is not open in 1 sec it will throw timeout error
    driver.get("http://www.thetestingworld.com/testings")
    #driver.implicitly_wait(20) #by default for object wait is 0 seconds this is like maximum time out to wait for that element or locator
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):

    #Fetching Title
    print("Title of page is "+ driver.title)

    #Fetch Url of page
    print("Page url is "+ driver.current_url)

    #Fetch complete page html source code
    print("***********************************")
    print(driver.page_source)

    #Fetch element/locator text
    print(driver.find_element_by_class_name("displayPopup").text) #using text property

    #Fetching attribute(s)value of element by locating it
    print("Value of button is "+ driver.find_element_by_xpath("//input[@type='submit']").get_attribute("value"))

    #Fetch all available values from dropdown
    # to work on drop-down, list (only by index, value & visible text)
    wait = WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element((By.NAME,'sex'), 'Male'))
    obj = Select(driver.find_element_by_name("sex"))
    obj.select_by_visible_text("Male")

    wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'), 'India'))
    obj1 = Select(driver.find_element_by_xpath("//select[@id = 'countryId']"))
    obj1.select_by_visible_text("India")

    wait.until(ec.text_to_be_present_in_element((By.ID,'stateId'), 'Delhi'))
    obj2 = Select(driver.find_element_by_xpath("//select[@id = 'stateId']"))
    obj2.select_by_visible_text("Delhi")

    #time.sleep(20) #This is hardcoded wait or forceful wait

    #Fetch selected option
    print(obj.first_selected_option.text)

    #Fetch all available options in the drop down
    print(obj.options) #it will not work as it will return only object

    for opt in obj.options:
        print(opt.text)

    assert driver.current_url == "http://www.thetestingworld.com/testings/"