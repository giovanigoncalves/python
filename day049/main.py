from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep


service = Service("/home/giovani/Softwares/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3318540929&f_AL=true&f_C=%5B%5D&f_E=%5B%5D&f_EA=%5B%5D&f_F=%5B%5D&f_I=%5B%5D&f_JC=%5B%5D&f_JIYN=%5B%5D&f_JT=%5B%5D&f_PP=%5B%5D&f_T=%5B%5D&f_WT=%5B%5D&keywords=python%20developer&sortBy=R")
driver.maximize_window()

sleep(3)
sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button.click()
sleep(1)



email = driver.find_element(By.ID, "username")
email.send_keys("put_your_email_here")
password = driver.find_element(By.ID, "password")
password.send_keys("put your email password here")
sign_in = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container  .btn__primary--large")
sign_in.click()
sleep(3)

# hide_message = driver.find_element(By.CLASS_NAME, "mercado-match")
# hide_message.click()

job_list = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
# print(len(job_list))
title = []
for job in job_list:
    sleep(1.)
    if len(job.get_attribute("class")) != 0 and "ember-view   jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item" in job.get_attribute("class"):
        job.click()
        title_job = driver.find_element(By.CSS_SELECTOR, '#ember130 h2').text
        title.append(title_job)
        save = job.find_element(By.CSS_SELECTOR, 'button span')
        save.click()
        sleep(1.)
