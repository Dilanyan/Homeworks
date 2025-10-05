from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException

driver = webdriver.Firefox()
try:
    # Step 1
    driver.get("https://demoqa.com/frames")
    driver.maximize_window()
    iframe1 = driver.find_element(By.ID, "frame1")
    driver.switch_to.frame(iframe1)
    el_h1 = driver.find_element(By.ID, "sampleHeading")
    print(el_h1.text)
    assert el_h1.text == "This is a sample page"
    driver.switch_to.default_content()
    driver.get("https://demoqa.com/alerts")
    el_time_alert_button = driver.find_element(By.ID, "timerAlertButton")
    el_time_alert_button.click()
    sleep(6)
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    assert alert_window.text == "This alert appeared after 5 seconds"
    alert_window.accept()

    # Step 2
    driver.get("https://demoqa.com/browser-windows")
    main_window_handler = driver.current_window_handle
    el_h1 = driver.find_element(By.XPATH, "//div[@id = 'browserWindows'] / h1")
    print(el_h1.text)
    assert el_h1.text == "Browser Windows"
    driver.switch_to.new_window("tab")
    driver.get("https://demoqa.com/alerts")
    el_alert_button = driver.find_element(By.ID, "alertButton")
    el_alert_button.click()
    sleep(1)
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    assert alert_window.text == "You clicked a button"
    alert_window.accept()
    driver.close()
    driver.switch_to.window(main_window_handler)
    el_h1 = driver.find_element(By.XPATH, "//div[@id = 'browserWindows'] / h1")
    print(el_h1.text)
    assert el_h1.text == "Browser Windows"

    # Step 3
    driver.get("https://demoqa.com/browser-windows")
    main_window_handler = driver.current_window_handle
    el_h1 = driver.find_element(By.XPATH, "//div[@id = 'browserWindows'] / h1")
    print(el_h1.text)
    assert el_h1.text == "Browser Windows"
    el_new_window_button = driver.find_element(By.XPATH, "//button[@id = 'windowButton']")
    el_new_window_button.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    el_h1 = driver.find_element(By.XPATH, "//*[@id = 'sampleHeading']")
    print(el_h1.text)
    assert el_h1.text == "This is a sample page"
    driver.close()
    driver.switch_to.window(main_window_handler)
    el_h1 = driver.find_element(By.XPATH, "//div[@id = 'browserWindows'] / h1")
    print(el_h1.text)
    assert el_h1.text == "Browser Windows"

    # Step 4
    driver.get("https://demoqa.com/frames")
    el_h1 = driver.find_element(By.XPATH, "//div[@id = 'framesWrapper'] / h1")
    print(el_h1.text)
    assert el_h1.text == "Frames"
    iframe1 = driver.find_element(By.ID, "frame1")
    driver.switch_to.frame(iframe1)
    el_h1 = driver.find_element(By.ID, "sampleHeading")
    print(el_h1.text)
    assert el_h1.text == "This is a sample page"

    driver.switch_to.default_content()
    iframe2 = driver.find_element(By.ID, "frame2")
    print(iframe2.get_attribute("width"))
    driver.switch_to.frame(iframe2)
    el_h1 = driver.find_element(By.ID, "sampleHeading")
    print(el_h1.text)
    assert el_h1.text == "This is a sample page"

    driver.switch_to.default_content()
    el_h1 = driver.find_element(By.XPATH, "//div[@id = 'framesWrapper'] / h1")
    print(el_h1.text)
    assert el_h1.text == "Frames"
    print("Iframe task completed")


    # Step 5
    driver.get("https://demoqa.com/alerts")
    el_alert_button = driver.find_element(By.ID, "alertButton")
    el_alert_button.click()
    sleep(1)
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    assert alert_window.text == "You clicked a button"
    alert_window.accept()

    el_alert_confirm_box_button = driver.find_element(By.ID, "confirmButton")
    el_alert_confirm_box_button.click()
    sleep(1)
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    assert alert_window.text == "Do you confirm action?"
    alert_window.dismiss()

    el_confirm_result = driver.find_element(By.CSS_SELECTOR, "#confirmResult")
    print(el_confirm_result.text)
    assert el_confirm_result.text == "You selected Cancel"



except (
        NoSuchElementException,
        ElementClickInterceptedException,
        ElementNotInteractableException
) as e:
    print(f"----------> {e} <----------")
finally:
    driver.quit()