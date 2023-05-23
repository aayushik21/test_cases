from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    basic_auth = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Basic Auth')
    ))
    basic_auth.click()

    driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

    success = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'example')
    ))

    assert 'Congratulations!' in success.text


finally:
    driver.quit()