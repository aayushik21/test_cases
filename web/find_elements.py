from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get('https://the-internet.herokuapp.com')
    driver.find_element(By.LINK_TEXT, 'Context Menu')

    els = driver.find_elements(By.TAG_NAME, 'a')
    print(f'There were {len(els)} anchor elements')

    els = driver.find_elements(By.TAG_NAME, 'jam')
    print(f'There were {len(els)} foo elements')
finally:
    driver.quit()