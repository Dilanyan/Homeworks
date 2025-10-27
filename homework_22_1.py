from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException

driver = webdriver.Firefox()
try:
    # Step 1
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    e_full_name1 = driver.find_element(By.XPATH, "//form[@id='userForm']/descendant::input[@id='userName']")
    e_full_name2 = driver.find_element(By.XPATH, "//form[@id='userForm']/descendant::input[1]")
    e_full_name3 = driver.find_element(By.XPATH, "//form[@id='userForm']/child::div[1]/child::div[2]/input")
    e_full_name4 = driver.find_element(By.XPATH, "//div[@id='userEmail-wrapper']/parent::form/child::div[1]/child::div[2]/input")
    e_full_name5 = driver.find_element(By.XPATH, "//div[@id='currentAddress-wrapper']/ancestor::div[@class='text-field-container']/descendant::input[1]")
    e_full_name6 = driver.find_element(By.XPATH, "//input[@id='userName']/parent::div")
    print(e_full_name6.get_attribute("class"))
    assert e_full_name6.get_attribute("class") == "col-md-9 col-sm-12"
    sleep(2)

    # Step 2
    driver.switch_to.new_window('tab')
    driver.get("https://demoqa.com/radio-button")
    sleep(2)
    e_h1 = driver.find_element(By.XPATH, "//h1")
    print(e_h1.text)
    assert e_h1.text == "Radio Button"
    e_radio_label = driver.find_element(By.XPATH, "//input[@id='yesRadio']/following::label[1]")
    e_radio_label1 = driver.find_element(By.XPATH, "//input[@id='yesRadio']/following-sibling::label")
    print(e_radio_label.text)
    assert e_radio_label1.text == "Yes"
    sleep(2)

    # Step 3
    driver.switch_to.new_window('tab')
    driver.get("https://demoqa.com/checkbox")
    e_h1 = driver.find_element(By.XPATH, "//h1")
    print(e_h1.text)
    assert e_h1.text == "Check Box"
    expand_all = driver.find_element(By.XPATH, "//button[@title='Expand all']")
    expand_all.click()
    sleep(2)
    e_spans = driver.find_elements(By.XPATH, "//span[text()='Home']/following::span")
    print(len(e_spans))
    driver.close()
    driver.switch_to.window(driver.window_handles[1])

    #step 4
    sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Step 5
    sleep(2)
    driver.close()

except (
        NoSuchElementException,
        ElementClickInterceptedException,
        ElementNotInteractableException
) as e:
    print(f"----------> {e} <----------")
finally:
    driver.quit()