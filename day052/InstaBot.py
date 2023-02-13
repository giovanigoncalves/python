import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

DATA = pd.read_csv(r'C:\Users\T-Gamer\Documents\data\data.txt')
CHROME_DRIVER_PATH = "/home/giovani/Softwares/chromedriver_linux64/chromedriver"
SIMILAR_ACCOUNT = 'playstation'
USERNAME = DATA.insta_user
PASSWORD = DATA.insta_password


class InstaFollower:
    
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        
    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        put_username = self.driver.find_element(By.NAME, "username")
        put_username.send_keys(USERNAME)
        sleep(.5)
        put_password = self.driver.find_element(By.NAME, "password")
        put_password.send_keys(PASSWORD)
        sleep(2)
        enter_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        enter_button.click()
        sleep(5)      
        
        
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        sleep(5)
        
         
        #  Por algum motivo, que ainda desconheço, não consigo clicar nos botões com a função a seguir:
         
'''   
    def follow(self):
        followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        sleep(2)
        i = 0
        for people in followers:
            if people.text == "Seguir":
                people.click()
                i += 1
            sleep(2)
        print(f"Seguindo {i} novos contatos")
        sleep(5)'''
   
        