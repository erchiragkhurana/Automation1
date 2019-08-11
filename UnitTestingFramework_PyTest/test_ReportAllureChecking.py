from selenium.webdriver import Chrome
import pytest
import allure



def test_set_path():
    global driver
    path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield #after yield, code will execute after every test case
    driver.close()

def test_chirag(set_path):
    driver.get("http://www.thetestingworld.com")
    driver.maximize_window()

def test_khurana(set_path):
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()

def test_chiragkhurana(set_path):
    driver.get("http://www.thetestingworld.com/aboutus")
    driver.maximize_window()