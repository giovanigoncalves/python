from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep 
from datetime import date
import pandas as pd

data = pd.read_csv(r'C:\Users\T-Gamer\Documents\data\data.txt')

service = Service("/home/giovani/Softwares/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3477237770&f_JT=C&keywords=data%20science")
driver.maximize_window()

sleep(3)
sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button.click()
sleep(1)



email = driver.find_element(By.ID, "username")
email.send_keys(data.username)
password = driver.find_element(By.ID, "password")
password.send_keys(data.password)
sign_in = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container  .btn__primary--large")
sign_in.click()
sleep(12)


job_list = driver.find_elements(By.CSS_SELECTOR, "ul.scaffold-layout__list-container li.ember-view")


title_job = []
company_name = []
job_location = []
for job in job_list:
    job.click()
    job.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2.t-24').text
    title_job.append(title)
    print(title)
    company = driver.find_element(By.CSS_SELECTOR, 'span.jobs-unified-top-card__company-name a').text
    company_name.append(company)
    location = driver.find_element(By.CSS_SELECTOR, 'span.jobs-unified-top-card__bullet').text
    job_location.append(location)
    print(location)
    
    text_saved = driver.find_element(By.CSS_SELECTOR, 'div.mt5 button.jobs-save-button span').text
    print(text_saved)
    sleep(2.5)
    if text_saved == 'Salvar':
        save_button = driver.find_element(By.CSS_SELECTOR, 'div.mt5 button.jobs-save-button span')
        save_button.click()
        print("Saved!")
    else:
        print(f"{title} already saved!")
        
    sleep(3)


# for job in title_job:
#     print(job)
    
# for company in company_name:
#     print(company)
    
# for location in job_location:
#     print(location)
    
with open(f"./jobs_list_{date.today()}.txt", "w", encoding="utf-8") as job_list_today:
    job_list_today.writelines(f"job;location;company\n")
    for i in range(len(title_job)):
        job_list_today.writelines(f"{title_job[i]};{job_location[i]};{company_name[i]}\n")
    