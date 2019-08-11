from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

path = "C:\\Users\\chirag\\Downloads\\chromedriver_win32\\chromedriver.exe"
#Step 1 is to open chrome browser
driver = Chrome(executable_path=path)

#Step 2 is to enter URL
driver.get("http://www.thetestingworld.com/testings")

#Step 3 is to maximize browser
driver.maximize_window()

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
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")

#Fetch selected option
print(obj.first_selected_option.text)

#Fetch all available options in the drop down
print(obj.options) #it will not work as it will return only object

for opt in obj.options:
    print(opt.text)
