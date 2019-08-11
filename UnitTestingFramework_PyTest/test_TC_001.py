#Using PyTest framework will help us in following ways:-
# 1. Options to conditionally execute test cases
# 2. Can setup pre-requisite and post script
# 3. Can add assertions
# 4. Options to generate report

#Naming conventions and some rules if you are using PyTest unittest framework
# 1. Test case file name should starts with test
# 2. Test case method name must start with test
# 3. If you want to run your test case from terminal or command prompt then just write pytest and execute it
# 4. pytest -v is to tell which is passed and which is skipped (verbose)
# 5. conditionally skip test cases then use skipif, if normal want to skip then skip
# 6. if you want to execute specific test case, then in terminal write pytest -k testcase/method name
# 7. if you want to execute tes cases with in which we have registration word them in terminal pytest -k registration -v
# 8. if you want to group some test cases and then want to execute specific group, then pyest -m Smoke(it is user defined)
# 9. if you want to execute all test cases except one group say Sanity, then pyest -m "not Sanity" -v
from selenium.webdriver import Chrome
import pytest

a = 101
@pytest.mark.skipif(a>100, reason="Don't want to execute in current build")
def test_registration_valid_data():
    path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()

@pytest.mark.skip("Don't want to execute in current build")
def test_registration_invalid_data():
    path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()

@pytest.mark.Smoke
def test_valid_data():
    path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()

@pytest.mark.Sanity
def test_invalid_data():
    path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()

@pytest.mark.Smoke
def test_invalid_data1():
    path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()