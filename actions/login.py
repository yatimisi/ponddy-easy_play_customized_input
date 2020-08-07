from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def login(driver, account, password):
    driver.find_element_by_id('id_username').send_keys(account)
    driver.find_element_by_id('id_password').send_keys(password)
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, ' dashboard')))
    except TimeoutException:
        return TimeoutException
