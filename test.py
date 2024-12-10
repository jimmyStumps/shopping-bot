from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get('https://www.kmart.com.au')

print(driver.page_source)

search_box = driver.find_element(By.CSS_SELECTOR, 'input[class=MuiInputBase-input]')
search_box.send_keys('yarn')
search_box.submit()

soup = BeautifulSoup(driver.page_source, 'html.parser')

prices = []

for item in soup.find_all('div', {'class': 's-result-item'}):
    price = item.find('span', {'class': 'a-offscreen'})
    if price:
        prices.append(float(price.text.replace('$', '')))

cheapest_price = min(prices)
print(f'The cheapest price is ${cheapest_price:.2f}')
