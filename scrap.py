from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

def other_rows(id):
    return f'//*[@id="{id}"]/td[2]'

def find_task(current_bid,quest_number):
    # extracting values of each bid as required 
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="view-bid-posting"]/div[2]/div[2]/h1')))
    res = {}
    res['quest_number'] = quest_number
    res['est_value'] = current_bid.find_element(By.XPATH,'//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text
    res['description'] = current_bid.find_element(By.XPATH,'//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text
    res['closing_date'] = current_bid.find_element(By.XPATH,'//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]').text
    print(res)

def iterate_rows(driver):
    # for first row 
    driver.get('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="table_id"]/tbody/tr[1]/td[2]')))
    current_bid = driver.find_element(By.XPATH,'//*[@id="table_id"]/tbody/tr[1]/td[2]')
    current_bid.click()
    find_task(driver,current_bid.text)

    # for other remaining rows
    for id in range(1,6):
        driver.get('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')
        wait.until(EC.presence_of_element_located((By.XPATH,other_rows(id))))
        current_bid = driver.find_element(By.XPATH,other_rows(id))
        current_bid.click()
        find_task(driver,current_bid.text)

iterate_rows(driver)
