from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')

search_box = driver.find_element_by_id('twotabsearchbox')
search_box.send_keys('yarn')
search_box.submit()

soup = BeautifulSoup(driver.page_source, 'html_parser')
prices = []

for item in soup.find_all('div', {'class': 's-result-item'}):
    price = item.find('span', {'class': 'a-offscreen'})
    if price:
        prices.append(float(price.text.replace('$', '')))

cheapest_price = min(prices)
print(f'The cheapest price is ${cheapest_price:.2f}')
