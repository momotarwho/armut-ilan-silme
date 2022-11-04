from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)


driver.get("https://armut.com/giris")

time.sleep(2)

driver.find_element(By.ID, "ContentPlaceHolder1_ucLogin_UserName").send_keys("mail adresi")
driver.find_element(By.ID, "ContentPlaceHolder1_ucLogin_Password").send_keys("şifre")
time.sleep(2)
driver.find_element(By.ID, "ContentPlaceHolder1_ucLogin_LoginButton").click()
time.sleep(10)
driver.find_element(By.CLASS_NAME, "opportunity-filter__filter").click()
time.sleep(20)




for i in range(100):
    driver.find_element(By.CLASS_NAME, "opportunity-card__container").click()
    time.sleep(7)
    driver.find_element(By.CLASS_NAME, "icon-trash").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "checkmark").click()
    time.sleep(3)
    driver.find_element(By.ID, "submit-no-thanks").click()
    time.sleep(2)