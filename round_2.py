from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def read_difficulty():
    # open website
    driver.get("https://mathup.com/games/crossbit?mode=championship")
    
    # click start button
    start_btn = wait.until(EC.visibility_of_element_located(START_BTN))
    start_btn.click()

    # read difficulty
    diff_val = wait.until(EC.visibility_of_element_located(DIFFICULTY_VALUE)).text
    return diff_val

def main_fun(n):
    for i in range(n):
        level = read_difficulty()
        print(f"Run {i+1} : Diffculty Level is {level}")
        
        

START_BTN = (By.XPATH, "//div[text()='Start']")
DIFFICULTY_VALUE = (By.XPATH, "//div[text()='Difficulty']/following-sibling::div")

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, timeout=20)
main_fun(10)
driver.quit()