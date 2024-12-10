from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.twitch.tv/")
search_box = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search Input"]')
search_box.send_keys(
    'fast painting'
)

search_button = driver.find_element(By.CSS_SELECTOR, 'button[icon="NavSearch"]')
search_button.click()

