from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException

driver = webdriver.Firefox()
try:
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    elements_cards = driver.find_elements(By.CLASS_NAME, "card")
    sleep(2)
    elements_cards[0].click()
    elements_url = driver.current_url
    assert "elements" in elements_url
    element_button = driver.find_element(By.ID, 'item-4')
    element_button.click()
    text_element_buttons = driver.find_element(By.TAG_NAME, "h1")
    assert text_element_buttons.is_displayed()
    button_click_me = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    button_click_me.click()
    text_click_me = driver.find_element(By.ID, "dynamicClickMessage")
    assert text_click_me.is_displayed()
    driver.switch_to.new_window('tab')
    driver.get("https://demoqa.com/radio-button")
    element_impressive_radio = driver.find_element(By.XPATH, "//label[text()='Impressive']")
    element_impressive_radio.click()
    element_impressive_text = driver.find_element(By.XPATH, "//span[text()='Impressive']")
    assert element_impressive_text.is_displayed()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    element_links = driver.find_element(By.ID, 'item-5')
    element_links.click()
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        print(link.text)

except (
        NoSuchElementException,
        ElementClickInterceptedException,
        ElementNotInteractableException
) as e:
    print(f"----------> {e} <----------")
finally:
    driver.quit()