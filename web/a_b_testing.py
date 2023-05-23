from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    a_b_testing = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'A/B Testing')
    ))
    a_b_testing.click()

finally:
    driver.quit()