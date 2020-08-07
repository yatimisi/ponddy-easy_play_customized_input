import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_url(driver, url):
    while(driver.current_url != url):
        time.sleep(1)


def wait_xpath(driver, xpath):
    WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
