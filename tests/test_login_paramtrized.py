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