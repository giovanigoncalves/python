from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import time, sleep


service = Service("/home/giovani/Softwares/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")
sleep(3)
print("Hello")

languages = driver.find_elements(By.CSS_SELECTOR, ".langSelectButton")
# print(languages)
for lang in languages:
    # print(lang.text)
    if lang.get_attribute("id") == "langSelect-EN":
        lang.click()
        break
sleep(5)
banner = driver.find_element(By.CSS_SELECTOR, ".cc_banner-wrapper a")
banner.click()

cookie_button = driver.find_element(By.ID, "bigCookie")

timeout = time() + 5
while True:
    cookie_button.click()

    if time() > timeout:
        number_cookies = int(driver.find_element(By.ID, "cookies").text.split()[0].strip())
        produts_available = {}
        for i in range(19):
            product_button = driver.find_element(By.ID, f"product{str(i)}")
            product_price = driver.find_element(By.ID, f"productPrice{str(i)}")
            price = int(product_button.text.split("\n")[1].strip().replace(",", ""))
            if price != "":
                produts_available[price] = "product{str(i)}"

        product_to_be_upgraded = []
        for value, name in produts_available.items():
            if number_cookies > value:
                product_to_be_upgraded.append(value)

        if len(product_to_be_upgraded) > 0:
            highest_value = max(product_to_be_upgraded)
            name_upgrade_product = produts_available[highest_value]
            product_button = driver.find_element(By.ID, f"{name_upgrade_product}")
            product_button.click()

        timeout += 5
# for i in products:
#     print(i.get_attribute("id"))

# while True:
#     cookie_button.click()
# cookies_button = driver.find_element(By.ID, "cookie")
# products = driver.find_elements(By.CSS_SELECTOR, "#store div")
# all_products = [item.get_attribute("id") for item in products]
# timeout = time() + 5
#
# while True:
#
#     cookies_button.click()
#
#     if time() > timeout:
#         all_values = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         products_value = [int(value.text.split("-")[1].strip().replace(",", "")) for value in all_values if value.text != ""]
#
#         cookies_upgrade = {}
#         for n in range(len(products_value)):
#             cookies_upgrade[products_value[n]] = all_products[n]
#
#         money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
#
#         items_to_be_upgraded = []
#         for value, item in cookies_upgrade.items():
#             if money > value:
#                 items_to_be_upgraded.append(value)
#         if len(items_to_be_upgraded) > 0:
#             highest_price_to_upgrade = max(items_to_be_upgraded)
#             item_to_upgrade = cookies_upgrade[highest_price_to_upgrade]
#             print(f"Highest price: {highest_price_to_upgrade}\nItem: {item_to_upgrade}")
#
#             up_click = driver.find_element(By.ID, f"{item_to_upgrade}")
#             up_click.click()
#
#         if money > 123456789:
#             break
#
#         timeout = time() + 5
# # for i in values:
# #     # i = i.split()[0].strip()
# #     teste = i.text
# #     print(teste)
# # print(int(driver.find_element(By.CSS_SELECTOR, "#store #buyCursor b").text.split("-")[1].strip()))
#
sleep(5)
# driver.quit()
# print("Finish")