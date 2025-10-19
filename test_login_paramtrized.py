from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.r
def test_saucedemo_login(driver, base_url, credentials):
    username, password, expected_result = credentials
    driver.get(base_url + "/login")
    wait = WebDriverWait(driver, 10)

    el_user_name_field = driver.find_element(By.XPATH, "//input[@id='userName']")
    wait_el_user_name_field = wait.until(EC.visibility_of(el_user_name_field))
    wait_el_user_name_field.send_keys(username)

    el_user_password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    wait_el_user_password_field = wait.until(EC.visibility_of(el_user_password_field))
    wait_el_user_password_field.send_keys(password)

    el_login_button = driver.find_element(By.XPATH, "//button[@id='login']")
    wait_el_login_button = wait.until(EC.visibility_of(el_login_button))
    wait_el_login_button.click()
    sleep(5)

    login_success = "profile" in driver.current_url
    print(f"\nBrowser: {driver.name} | User: {username} | Expected: {expected_result} | Actual: {login_success}")

    assert login_success == expected_result, f"Login result mismatch for {username} on {driver.name}"