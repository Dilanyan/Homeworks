# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_driver(browser="chrome"):
    if browser.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        # options.add_argument("user-data-dir=C:\\Users\\Narek\\AppData\\Local\\Google\\Chrome\\User Data")
        # options.add_argument("profile-directory=Profile 2")
        return webdriver.Chrome(options=options)
    if browser.lower() == "firefox":
        return webdriver.Firefox()
    if browser.lower() == "edge":
        return webdriver.Edge()
    if browser.lower() == "safari":
        return webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

@pytest.fixture(scope="function")
def driver():
    driver = get_driver(browser="chrome")
    """Launch Chrome browser for each test, and quit afterward."""
    print("\n[Setup] Launching Chrome browser...")
    yield driver
    print("[Teardown] Closing browser...")
    driver.quit()



@pytest.fixture(scope="session")
def base_url():
    """Provide base URL to be used across tests."""
    return "https://the-internet.herokuapp.com"

