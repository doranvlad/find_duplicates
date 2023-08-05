from fd_login import fd_login_def
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    driver = fd_login_def()

    elem_full = driver.find_element(By.NAME, 'full')
    elem_full.click()

    elem_search = driver.find_element(By.NAME, 'search')
    elem_search.send_keys('VPN110-1TBM28H')

    submit_button = driver.find_element(By.XPATH, "//input[@value='Найти']")
    submit_button.click()