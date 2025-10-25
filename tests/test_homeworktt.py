from time import sleep

import pytest
from pages.homeworktt import HomeWorkTT

@pytest.mark.stepone
@pytest.mark.regression
def test_step_1(driver):
    steps = HomeWorkTT(driver)
    steps.open_url_step1()
    steps.click_after_button_step1()
    assert steps.is_after_button_clickable(), "Button after not loaded properly"

@pytest.mark.steptwo
@pytest.mark.regression
def test_step_2(driver):
    steps = HomeWorkTT(driver)
    steps.open_url_step2()
    steps.click_start_button_step2()
    steps.get_h4_text_step2()
    assert steps.get_h4_text_step2(), "Hello World!"

@pytest.mark.stepthree
@pytest.mark.regression
def test_step_3(driver):
    steps = HomeWorkTT(driver)
    steps.open_url_step3()
    steps.click_for_js_alert_button_step3()
    steps.alert()
    print(steps.get_alert_text_step3())
    assert steps.get_alert_text_step3() == "I am a JS Alert"
    steps.accept_alert_step3()
    assert steps.get_result_text_step3() == "You successfully clicked an alert"

@pytest.mark.four
@pytest.mark.regression
def test_step_4(driver):
    steps = HomeWorkTT(driver)
    steps.open_url_step4()
    assert steps.is_ghost_element_there() == False, "Ghost element should not be there"


