from time import sleep
import pytest
from selenium.webdriver.common.by import By


class Selenium_helper():
    """
        In this class collected all methods that will help to do something related to the selenium part of our project, for example:
         open/close webdriver/browser/tab,
         go to webpage
         do some clicks
         return text
         ...
    """
    @staticmethod
    def do_some_rutin(driver):
        try:
            driver.get("https://www.armstqb.org/")
            driver.maximize_window()
            current_title = driver.title
            print("Title", current_title)
            assert "ArmSTQB" in current_title
            driver.switch_to.new_window('tab')
            driver.get("https://www.armstqb.org/partners")
            sleep(3)
            current_url = driver.current_url
            print("Current URL:", current_url)
            assert "https://www.armstqb.org/partners" in current_url
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.minimize_window()
        finally:
            driver.quit()



    @staticmethod
    def button_click(driver, button_name):
        button = driver.find_element(By.XPATH, f"//button[text()='{button_name}']")
        button.click()
        sleep(5)

    @staticmethod
    def message_assertion(driver, message_text):
        p_element = driver.find_element(By.CSS_SELECTOR, "p[id='message']")
        assert p_element.is_displayed()
        assert p_element.text in message_text

    @staticmethod
    def click_checkbox(driver):
        checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox.click()

    @staticmethod
    def type_text_in_text_field(driver, text):
        input_text_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        input_text_field.send_keys(text)

