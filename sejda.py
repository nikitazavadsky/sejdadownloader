from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

import os

def download_file(url: str):

    options = webdriver.ChromeOptions() 

    prefs = {"download.default_directory" : os.getcwd()}
    options.add_experimental_option("prefs", prefs);

    driver = webdriver.Chrome(options=options)

    # Navigate to the webpage
    driver.get(url)  # Replace with the actual URL of the webpage
    sleep(2)

    # Find the download button using XPath or CSS selector
    download_button = driver.find_element(By.CLASS_NAME, "download-share-btn")  # Replace with the appropriate XPath
    download_button.click()
    sleep(5)

    # Close the browser
    driver.quit()
