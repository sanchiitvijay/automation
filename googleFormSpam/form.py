from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://forms.gle/mR5wAFuMqDuvDVto7") #give the form parth

# change the aria-labelledBy according to the form

wait = WebDriverWait(driver, 5)

# for input field
name_field = driver.find_element(By.XPATH, "//input[@aria-labelledby='i1']")
email_field = driver.find_element(By.XPATH, "//input[@aria-labelledby='i33']")
message_field = driver.find_element(By.XPATH, "//textarea[@aria-labelledby='i37']")

name_field.send_keys("Sanchit Vijay")
email_field.send_keys("sanchiitvijay@gmail.com")
message_field.send_keys("This is a test message")

# for checkboxes
checkbox = driver.find_element(By.XPATH, "//div[@data-answer-value='hindi']")
checkbox.click()


# for radio button
radio_button = driver.find_element(By.XPATH, "//div[@data-value='red']")
radio_button.click()

# for dropdown (not working idk why)

# dropdown_button = driver.find_element(By.XPATH, "//div[@aria-describedby='i30 i31']")
# dropdown_button.click()
# dropdown = driver.find_element(By.XPATH, "//span[contains(text(), '2026')]")
# dropdown.click()

submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit_button.click()

driver.quit()
