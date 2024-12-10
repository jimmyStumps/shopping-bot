from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.twitch.tv/directory/game/Art")
driver.execute_script("""
    let items=document.querySelectorAll('.tw-tower>div');
    items[items.length-1].scrollIntoView();
    """)

