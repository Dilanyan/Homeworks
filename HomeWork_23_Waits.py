from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


driver = get_driver(browser="chrome")

try:
    # Step 1
    driver.get("https://demoqa.com/dynamic-properties")
    driver.implicitly_wait(10)
    el_button = driver.find_element(By.ID, "visibleAfter")
    el_button.click()

    # Step 2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    el_button = driver.find_element(By.TAG_NAME, "button")
    el_button.click()
    wait = WebDriverWait(driver, 10)
    # el_h4 = driver.find_element(By.XPATH, "//div[@id='finish']/h4")
    # el_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
    # el_text1 = wait.until(EC.visibility_of(el_h4))
    el_text2 = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='finish']/h4"), "Hello World!"))
    print(el_text2)
    # assert el_text == "Hello World!"

    # Step 3
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    el_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    el_button.click()
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    print("Alert text:", alert.text)
    assert alert.text == "I am a JS Alert"
    alert.accept()
    el_result = driver.find_element(By.ID, "result")
    print(el_result.text)
    assert el_result.text == "You successfully clicked an alert"

    # Step 4
    driver.get("https://demoqa.com/automation-practice-form")
    el_ghost = driver.find_element(By.XPATH, "//button[text()='Ghost']")

except (
        TimeoutException
) as e:
    print(f"----------> {e} <----------")
except NoSuchElementException:
    print("Element not found!")
finally:
    driver.quit()