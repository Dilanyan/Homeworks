from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomeWorkTT(BasePage):

    START_BUTTON = (By.XPATH, "//button")
    H4 = (By.XPATH, "//div[@id='finish']/h4")
    ENABLE_AFTER = (By.ID, "enableAfter")
    FOR_JS_ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    RESULT_TEXT = (By.ID, "result")
    TEXT_GHOST = (By.XPATH, "//button[text()='Ghost']")

    # --------------- Step 1 -----------------------
    def open_url_step1(self):
        self.open("https://demoqa.com/dynamic-properties")

    def click_after_button_step1(self):
        self.is_visible(self.ENABLE_AFTER)
        self.click(self.ENABLE_AFTER)

    def is_after_button_clickable(self):
        return self.is_clickable(self.ENABLE_AFTER)

    # --------------- Step 2 -----------------------
    def open_url_step2(self):
        self.open("https://the-internet.herokuapp.com/dynamic_loading/1")

    def click_start_button_step2(self):
        self.click(self.START_BUTTON)

    def get_h4_text_step2(self):
        self.is_visible(self.H4)
        return self.get_text(self.H4)

    # --------------- Step 3 -----------------------
    def open_url_step3(self):
        self.open("https://the-internet.herokuapp.com/javascript_alerts")

    def click_for_js_alert_button_step3(self):
        self.click(self.FOR_JS_ALERT_BUTTON)

    def get_alert_text_step3(self):
        return self.alert().text

    def accept_alert_step3(self):
        self.alert().accept()

    def get_result_text_step3(self):
        return self.get_text(self.RESULT_TEXT)

    # --------------- Step 4 -----------------------
    def open_url_step4(self):
        self.open("https://demoqa.com/automation-practice-form")

    def is_ghost_element_there(self):
        return self.is_visible(self.TEXT_GHOST)