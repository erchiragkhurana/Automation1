from selenium.webdriver import Chrome
import pytest

#if you want to run this method before and after each test case in wtest_002_Fixtures_beforeaftermethod.pyhich we mention method name
@pytest.fixture(scope="module")#if you write scope = "module" in bracket then before yield method will run only once then it will run all other test cases, then only once after yield path
def set_path():
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