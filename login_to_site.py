from selenium import webdriver
from selenium.webdriver.common.by import By
import json


def fd_login_def():
    with open('auth.json', 'r', encoding='utf-8') as file1:
        auth = json.load(file1)

    driver = webdriver.Firefox()

    driver.get(auth["path"])

    element_login = driver.find_element(By.NAME, 'name')
    element_login.send_keys(auth["name"])

    element_password = driver.find_element(By.NAME, 'pas')
    element_password.send_keys(auth["pas"])

    element_button = driver.find_element(By.NAME, 'login')
    element_button.click()

    driver.get(auth["path"])
    return driver
