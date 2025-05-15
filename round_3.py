import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_page_load_time():
    start_time = time.time()
    
    #Load webpage and wait until START button appears
    driver.get("https://mathup.com/games/crossbit?mode=daily_challenge")
    wait.until(EC.visibility_of_element_located(START_BTN))
    
    end_time = time.time()
    load_time = round(end_time - start_time, 2)
    return load_time

def main_fun(n):
    load_times = []
    
    for i in range(n):
        load_time = read_page_load_time()
        print(f"Run {i+1}: Load time is {load_time} sec")
        load_times.append(load_time)
    
    avg_time = round(sum(load_times) / len(load_times), 2)
    print(f"Average Load time is {avg_time} sec")
    
    

START_BTN = (By.XPATH, "//div[text()='Start']")

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, timeout=20)
main_fun(10)
driver.quit()