from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920, 1080")
options.add_argument("start-maximized")
options.add_experimental_option(
   "prefs", {"profile.managed_default_content_settings.images": 2}
)

driver = webdriver.Chrome(options=options)
driver.get("https://www.twitch.tv/directory/game/Art")
element = WebDriverWait(driver=driver, timeout = 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-target=directory-first-item]'))
)

sel = Selector(text=driver.page_source)
parsed = []
for item in sel.xpath("//div[contains(@class, 'tw-tower')]/div[@data-target]"):
    parsed.append({
        'title': item.css('h3::text').get(),
        'url': item.css('.tw-link::attr(href)').get(),
        'username': item.css('.tw-link::text').get(),
        'tags': item.css('.tw-tag ::text').getall(),
        'viewers': ''.join(item.css('.tw-media-card-stat::text').re(r'(\d+)')),
    })

print(parsed)

driver.quit()
