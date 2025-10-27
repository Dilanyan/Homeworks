import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.sa
@pytest.mark.regression
def test_step_1(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    driver.implicitly_wait(10)
    el_button = driver.find_element(By.ID, "enableAfter")
    el_button.click()

@pytest.mark.sb
@pytest.mark.regression
def test_step_2(driver, base_url):
    driver.get(base_url + "/dynamic_loading/1")
    el_button = driver.find_element(By.TAG_NAME, "button")
    el_button.click()
    wait = WebDriverWait(driver, 10)
    el_h4 = driver.find_element(By.XPATH, "//div[@id='finish']/h4")
    # el_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
    el_text1 = wait.until(EC.visibility_of(el_h4))
    # el_text2 = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='finish']/h4"), "Hello World!"))
    print(el_text1.text)
    # assert el_text == "Hello World!"

@pytest.mark.sc
@pytest.mark.regression
def test_step_3(driver, base_url):
    driver.get(base_url + "/javascript_alerts")
    wait = WebDriverWait(driver, 10)
    el_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    wait_el_button = wait.until(EC.visibility_of(el_button))
    wait_el_button.click()
    alert = wait.until(EC.alert_is_present())
    print("Alert text:", alert.text)
    assert alert.text == "I am a JS Alert"
    alert.accept()
    el_result = driver.find_element(By.ID, "result")
    print(el_result.text)
    assert el_result.text == "You successfully clicked an alert"

@pytest.mark.sd
@pytest.mark.regression
def test_step_4(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    el_ghost = driver.find_element(By.XPATH, "//button[text()='Ghost']")


