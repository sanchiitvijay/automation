from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


driver = webdriver.Chrome()

os.makedirs("data", exist_ok=True)

query = "monitor"
file = 0

for i in range(1,5):

    driver.get(f"https://www.flipkart.com/search?q=monitor&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")

    elems = driver.find_elements(By.CLASS_NAME,"cPHDOP")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        if d is not None:
            with open(f"data/{query}_{file}.html","w", encoding="utf-8") as f:
                f.write(d)
            file += 1
driver.quit()