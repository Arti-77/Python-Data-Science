from selenium import webdriver
from selenium.webdriver.common.by import By
home_url = 'https://www.amazon.in'
driver.get(home_url)

search_box = driver.find_element(By.NAME)
print(driver.title)
try:
    ele=driver.find_element(By.TAG_NAME,'h1')
    print(ele.text)
except Exceptional as e:
        print(e)
driver.close()