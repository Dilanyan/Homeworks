from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.XPATH, "//input[@id='userName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login']")
    ERROR_MESSAGE = (By.XPATH, "//p[@id='name']")
    USER_NAME = (By.XPATH, "//label[@id='userName-value']")

    def open_login_page(self):
        self.open("https://demoqa.com/login")

    def login(self, username, password):
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        self.is_visible(self.USER_NAME)

    def is_loaded(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)

    def get_error_text(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_user_login(self):
        return self.is_visible(self.USER_NAME)