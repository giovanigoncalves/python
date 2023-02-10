from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd 

DATA = pd.read_csv(r'C:\Users\T-Gamer\Documents\data\data.txt')
PROMISED_DOWN = 100
PROMISED_UP = 50
CHROME_DRIVER_PATH = "/home/giovani/Softwares/chromedriver_linux64/chromedriver"
TWITTER_EMAIL = DATA.username_twiter
TWITTER_PASSWORD = DATA.password



class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.down = 0
        self.up = 0
        
    def message(self, download, upload):
        return f"Hello, @internetprovider! My internet is with {download}/{upload} Mb, while I pay for {PROMISED_DOWN}/{PROMISED_UP} Mb."
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/pt")
        sleep(3)
        initiate_test_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        initiate_test_button.click()
        sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(self.down)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
        sleep(2)
        
        
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoicHQifQ%3D%3D%22%7D")
        self.driver.maximize_window()

        sleep(3)

        put_user = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        put_user.send_keys(TWITTER_EMAIL)
        sleep(1.5)
        advance_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        advance_button.click()
        sleep(1.5)

        put_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        put_password.send_keys(TWITTER_PASSWORD)
        sleep(1.5)
        enter_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span')
        enter_button.click()

        sleep(5)

        twitter_text = self.driver.find_element(By.CSS_SELECTOR, 'div .public-DraftStyleDefault-block')
        twitter_text.send_keys(self.message(self.down,self.up))
        publish_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        publish_button.click()
        sleep(20)