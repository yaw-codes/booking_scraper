#!/usr/bin/env python3
"""
Author : stan <stan@localhost>
Date   : 2024-06-25
Purpose: Booking Spider
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import os

from bs4 import BeautifulSoup

import time
import argparse

service = Service(executable_path='./chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(service=service)
# use to change the webdriver wait times
wait = WebDriverWait(driver, 30)
# adjust this based on connection speed

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Booking Spider',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('url',
                        metavar='url',
                        default="https://www.mayslimo.com/online-booking/",
                        help='url of website')


    return parser.parse_args()


def switch_to_frame():
    wait.until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, 'iFrameResizer0')))
    # driver.switch_to.frame(iframe)

# select service type
def select_service():
    # wait for the precense of element to be located
    wait.until(EC.presence_of_element_located((By.ID, 'ServiceTypeId')))

    # Locate the drop-down menu to select the location
    # Replace with the actual ID of the drop-down
    dropdown_element = driver.find_element(By.ID, 'ServiceTypeId')

    # Creating a Select object
    select = Select(dropdown_element)

    # select by index (0-based index)
    select.select_by_index(1)

    # Locate the date input field by its ID

    # wait for the prescence of an element if what what we're looking for doesn't exist yet

# --------------------------------------------------
def main():
    args = get_args()

    try:
        driver.maximize_window()
        driver.get(args.url)
        switch_to_frame()

    except Exception as ex:
        print(ex)

    finally:
        
        driver.close()
        driver.quit()




# --------------------------------------------------
if __name__ == '__main__':
    main()
