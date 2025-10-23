# conftest.py
import os
import datetime
import base64
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(browser="chrome"):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # options.add_argument("--incognito")
    # options.add_argument("user-data-dir=C:\\Users\\Narek\\AppData\\Local\\Google\\Chrome\\User Data")
    # options.add_argument("profile-directory=Profile 2")
    if browser.lower() == "chrome":
        return webdriver.Chrome(options=options)
    if browser.lower() == "firefox":
        return webdriver.Firefox()
    if browser.lower() == "edge":
        return webdriver.Edge(options=options)
    if browser.lower() == "safari":
        return webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

@pytest.fixture(params=["chrome"])
def driver(request):
    driver = get_driver(request.param)
    """Launch Chrome browser for each test, and quit afterward."""
    print("\n[Setup] Launching Chrome browser...")
    yield driver

    test_failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed
    if test_failed:
        screenshot_dir = "src/reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{request.node.name}_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, file_name)

        driver.save_screenshot(screenshot_path)
        print(f"📸 Screenshot saved to: {screenshot_path}")

        with open(screenshot_path, "rb") as f:
            img_data = base64.b64encode(f.read()).decode("utf-8")
            extra_html = pytest_html.extras.html(
            f'<div><b>Screenshot:</b><br><img src="data:image/png;base64,{img_data}" '
            f'style="width:600px;height:auto;border:1px solid #ccc"/></div>'
        )
        if hasattr(request.node, "extra"):
            request.node.extra.append(extra_html)
        else:
            request.node.extra = [extra_html]

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