# conftest.py
import pytest
from selenium import webdriver

def get_driver(browser="chrome"):
    if browser.lower() == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        # options.add_argument("--incognito")
        # options.add_argument("user-data-dir=C:\\Users\\Narek\\AppData\\Local\\Google\\Chrome\\User Data")
        # options.add_argument("profile-directory=Profile 2")
        return webdriver.Chrome(options=options)
    if browser.lower() == "firefox":
        return webdriver.Firefox()
    if browser.lower() == "edge":
        from selenium.webdriver.edge.options import Options
        options = Options()
        options.add_argument("--start-maximized")
        return webdriver.Edge(options=options)
    if browser.lower() == "safari":
        return webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

@pytest.fixture(params=["chrome", "edge", "firefox"])
def driver(request):
    driver = get_driver(request.param)
    driver.implicitly_wait(10)
    """Launch Chrome browser for each test, and quit afterward."""
    print("\n[Setup] Launching Chrome browser...")
    yield driver
    print("[Teardown] Closing browser...")
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    """Provide base URL to be used across tests."""
    # return "https://the-internet.herokuapp.com"
    return "https://demoqa.com"

@pytest.fixture(params=[
    ("tno", "A1b@cD3e", True),
    # ("tnt", "A1b@cD3e", True),
    # ("validName", "wrongPassword", True),
    # ("wrongName", "validPassword", False),
    ("wrongName", "wrongPassword", False),
])
def credentials(request):
    return request.param