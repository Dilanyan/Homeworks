from selenium_helper import Selenium_helper
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException

message_text_is_gone = "It's gone!"
driver = webdriver.Firefox()

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    driver.maximize_window()

    Selenium_helper.click_checkbox(driver)

    Selenium_helper.button_click(driver, "Remove")
    Selenium_helper.message_assertion(driver, message_text_is_gone)

    Selenium_helper.button_click(driver, "Add")
    Selenium_helper.message_assertion(driver, "It's back!")

    Selenium_helper.button_click(driver, "Remove")
    Selenium_helper.message_assertion(driver, message_text_is_gone)

    Selenium_helper.button_click(driver, "Enable")
    Selenium_helper.message_assertion(driver, "It's enabled!")

    Selenium_helper.type_text_in_text_field(driver, message_text_is_gone)

    Selenium_helper.button_click(driver, "Disable")
    Selenium_helper.message_assertion(driver, "It's disabled!")

except (
        NoSuchElementException,
        ElementClickInterceptedException,
        ElementNotInteractableException
) as e:
    print(f"----------> {e} <----------")
finally:
    driver.quit()