from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
   wait = WebDriverWait(driver, 10)
   driver.get('https://the-internet.herokuapp.com')
   add_remove_elements = wait.until(EC.presence_of_element_located(
      (By.LINK_TEXT, 'Add/Remove Elements')
   ))
   add_remove_elements.click()

   add_element = wait.until(EC.presence_of_element_located(
      (By.CSS_SELECTOR, 'button')
   ))
   add_element.click()
   add_element.click()
   add_element.click()
   add_element.click()
   add_element.click()


   delete1 = driver.find_element(By.ID, 'elements' )
   delete1.click()
   delete2 = driver.find_element(By.ID, 'elements' )
   delete2.click()
   delete3 = driver.find_element(By.ID, 'elements' )
   delete3.click()

finally:
   driver.quit()