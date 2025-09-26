from time import sleep
import pytest
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
