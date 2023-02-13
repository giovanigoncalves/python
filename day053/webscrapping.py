from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

HEADER = {
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "currency": "BRL"
}

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

URL_BASE = "https://www.zillow.com"
CHROME_DRIVER_PATH = "/home/giovani/Softwares/chromedriver_linux64/chromedriver"

class WebScrapper:
    
    def __init__(self):
        self.response = requests.get(URL, headers=HEADER)
        self.rental_list = self.response.text
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def track_web_info(self):
        soup = BeautifulSoup(self.rental_list, "html.parser")
        test = soup.findAll("script", attrs={"type": "application/json"})
        rent_data = test[1].text
        rent_data = rent_data.replace("<!--", "")
        rent_data = rent_data.replace("-->", "")
 
        rent_data = json.loads(rent_data)
        data_info = rent_data["cat1"]["searchResults"]["listResults"]
        self.addresses = [i["address"] for i in data_info]

        self.prices = []
        for i in data_info:
            try: 
                self.prices.append(i["price"])
            except KeyError:
                self.prices.append(i["units"][0]["price"]) 
                
        self.link = [URL_BASE + i["detailUrl"] for i in data_info]


    def fill_forms(self):
        
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfuItZUJlVtpPANVo7uxpcfbTEVk8VRFavrdqAa-Jk_2JJfxw/viewform?usp=sf_link")
        
        sleep(5)
        
        for item in range(len(self.addresses)):
            first_question = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            first_question.send_keys(f"{self.addresses[item]}")
            sleep(2)
            second_question = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            second_question.send_keys(f"{self.prices[item]}")
            sleep(2)
            third_question = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            third_question.send_keys(f"{self.link[item]}")
            sleep(2)            
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
            submit_button.click()
            sleep(2)
            submit_another = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            submit_another.click()
            sleep(2)