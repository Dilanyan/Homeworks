import pytest
from pages.login_page import LoginPage

@pytest.mark.r
def test_login(driver, credentials):
    username, password, expected_result = credentials
    login_page = LoginPage(driver)
    login_page.open_login_page()

    assert login_page.is_loaded(), "Login page not loaded properly"

    login_page.login(username, password)

    if expected_result:
        assert "profile" in driver.current_url, "User is not logged in"
    else:
        assert login_page.is_error_displayed(), "Error message not shown for invalid login"


    # el_user_name_field = driver.find_element(By.XPATH, "//input[@id='userName']")
    # wait_el_user_name_field = wait.until(EC.visibility_of(el_user_name_field))
    # wait_el_user_name_field.send_keys(username)
    #
    # el_user_password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    # wait_el_user_password_field = wait.until(EC.visibility_of(el_user_password_field))
    # wait_el_user_password_field.send_keys(password)
    #
    # el_login_button = driver.find_element(By.XPATH, "//button[@id='login']")
    # wait_el_login_button = wait.until(EC.visibility_of(el_login_button))
    # wait_el_login_button.click()
    # sleep(5)
    #
    # login_success = "profile" in driver.current_url
    # print(f"\nBrowser: {driver.name} | User: {username} | Expected: {expected_result} | Actual: {login_success}")
    #
    # assert login_success == expected_result, f"Login result mismatch for {username} on {driver.name}"