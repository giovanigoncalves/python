from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import time, sleep


service = Service("/home/giovani/Softwares/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookies_button = driver.find_element(By.ID, "cookie")
products = driver.find_elements(By.CSS_SELECTOR, "#store div")
all_products = [item.get_attribute("id") for item in products]
timeout = time() + 5
game_time = time() + 5*60

while True:

    cookies_button.click()

    if time() > timeout:
        all_values = driver.find_elements(By.CSS_SELECTOR, "#store b")
        products_value = [int(value.text.split("-")[1].strip().replace(",", "")) for value in all_values if value.text != ""]

        cookies_upgrade = {}
        for n in range(len(products_value)):
            cookies_upgrade[products_value[n]] = all_products[n]

        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        items_to_be_upgraded = []
        for value, item in cookies_upgrade.items():
            if money > value:
                items_to_be_upgraded.append(value)
        if len(items_to_be_upgraded) > 0:
            highest_price_to_upgrade = max(items_to_be_upgraded)
            item_to_upgrade = cookies_upgrade[highest_price_to_upgrade]

            up_click = driver.find_element(By.ID, f"{item_to_upgrade}")
            up_click.click()

        if time() > game_time:
            cps = driver.find_element(By.ID, "cps").text.split(":")[1].strip().replace(",", "")
            print(f"Cookies/second: {cps}")
            break

        timeout = time() + 5

driver.quit()
print("Finish")