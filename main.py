from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

print(driver.title)  # Título de la página
print(driver.current_url)  # URL de la página que está llamando

# Busco los elementos a los que les daré clic
time.sleep(2)

link_FirstName = driver.find_element(By.ID, "firstName") 
link_FirstName.send_keys("CRISTIAN")
time.sleep(1)

link_lastName = driver.find_element(By.ID, "lastName")
link_lastName.send_keys("CARPETA")
time.sleep(1)

link_email = driver.find_element(By.ID, "userEmail")
link_email.send_keys("CRISTIAN.CARPETA@YAHOO.COM")
time.sleep(2)

link_mobile = driver.find_element(By.ID, "userNumber")
link_mobile.send_keys("3022021545")
time.sleep(2)

link_subjet = driver.find_element(By.ID, "subjectsInput")
link_subjet.send_keys("Maths")
time.sleep(2)

link_current = driver.find_element(By.ID, "currentAddress")
link_current.send_keys("EL PROFE SEBASTIAN NO GASTA EMPANADA")
time.sleep(2)

link_submit = driver.find_element(By.ID, "submit")
link_submit.click()
time.sleep(2)


driver.quit()
