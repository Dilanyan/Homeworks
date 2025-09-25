from selenium import webdriver
from selenium_helper import Selenium_helper

drivers = [webdriver.Firefox(), webdriver.Chrome(), webdriver.Edge()]
for driver in drivers:
    Selenium_helper.do_some_rutin(driver)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')