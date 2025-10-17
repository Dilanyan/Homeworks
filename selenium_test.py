from time import sleep
from selenium.webdriver.common.by import By


def test_selen(driver):
    radio_button_and_assertion_text = "[text()='Impressive']"
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    elements_cards = driver.find_element(By.XPATH, "//h5[text()='Elements']")
    sleep(2)
    elements_cards.click()
    elements_url = driver.current_url
    assert "elements" in elements_url
    element_button = driver.find_element(By.CSS_SELECTOR, '#item-4')
    element_button.click()
    text_element_buttons = driver.find_element(By.CSS_SELECTOR, "div>h1[class='text-center']")
    assert text_element_buttons.is_displayed()
    button_click_me = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    button_click_me.click()
    text_click_me = driver.find_element(By.CSS_SELECTOR, "#dynamicClickMessage")
    assert text_click_me.is_displayed()
    driver.switch_to.new_window('tab')
    driver.get("https://demoqa.com/radio-button")
    element_impressive_radio = driver.find_element(By.XPATH, f"//label{radio_button_and_assertion_text}")
    element_impressive_radio.click()
    element_impressive_text = driver.find_element(By.XPATH, f"//span{radio_button_and_assertion_text}")
    assert element_impressive_text.is_displayed()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    element_links = driver.find_element(By.CSS_SELECTOR, '#item-5')
    element_links.click()
    links = driver.find_elements(By.CSS_SELECTOR, "div[id='linkWrapper'] > p > a")
    for link in links:
        print(link.text)