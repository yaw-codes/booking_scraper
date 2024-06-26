#!/usr/bin/env python
"""
Author : stan <stan@localhost>
Date   : 2024-06-25
Purpose: Booking Spider
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import os

from bs4 import BeautifulSoup

import time
import argparse

service = Service(executable_path='./chromedriver.exe')
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

    parser.add_argument('-u',
                        '--url',
                        metavar='url',
                        default="https://www.mayslimo.com/online-booking/",
                        help='URL of website')
    
    parser.add_argument('-s',
                        '--service_type',
                        help='Service type as an integer',
                        metavar='int',
                        choices=[x for x in range(0, 4)],
                        type=int,
                        default=1)
    
    parser.add_argument('-d',
                        '--date',
                        help='Date as a string in the form mm/dd/yyy',
                        metavar='date text',
                        type=str,
                        default='06/30/2024')
    parser.add_argument('-t',
                        '--time',
                        help='Time as a string in the form hh:mm AM',
                        metavar='time text',
                        type=str,
                        default="10:30 AM")
    parser.add_argument('-pl',
                        '--pickup_location_str',
                        help='pick up location as a string ',
                        metavar='pickup location text',
                        type=str,
                        default='ATL Airport')
    parser.add_argument('-dl',
                        '--dropoff_location_str',
                        help='dropoff location as a string ',
                        metavar='dropoff location text',
                        type=str,
                        default='sandy springs')

    return parser.parse_args()


def switch_to_frame():
    """switches to iframe for booking service"""
    wait.until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, 'iFrameResizer0')))

# select service type
def select_service(service_type):
    """selects service type"""
    # wait for the presence of element to be located
    wait.until(EC.presence_of_element_located((By.ID, 'ServiceTypeId')))

    # Locate the drop-down menu to select the location
    dropdown_element = driver.find_element(By.ID, 'ServiceTypeId')

    # Creating a Select object
    select = Select(dropdown_element)

    # select by index (0-based index)
    select.select_by_index(service_type)


def select_date(date_text):
    """Select the appropriate date"""
    wait.until(EC.presence_of_element_located((By.ID, 'PickUpDate')))

    date_input = driver.find_element(By.ID, 'PickUpDate')
    date_input.click()
    date_input.clear()

    # Optionally, you can use JavaScript to set the date if direct input doesn't work
    driver.execute_script(f"arguments[0].value = '{date_text}';", date_input)


def select_time(select_time):
    """Selects time for ride"""

    # Locate the input element by its ID
    time_input = driver.find_element(By.ID, 'PickUpTime')

    # Set the time value
    # Clear the field first (if necessary)
    time_input.clear()

    # # Enter the desired time in the format expected by the input field
    # time_input.send_keys('10:30 AM')  # Replace with your desired time format

    # Optionally, you can use JavaScript to set the time if direct input doesn't work
    driver.execute_script(f"arguments[0].value = '{select_time}';", time_input)

def pickUp_location(pickup_location_str):
    """Pickup location address"""
    # Locate the input element by its ID
    pickup_location_input = driver.find_element(By.ID, 'PickupLocation')

    # Set the input value
    pickup_location_input.clear()  # Clear the input field first, if necessary
    pickup_location_input.send_keys(pickup_location_str)

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//div[@id='PickupLocationSuggestionDiv']/ul//li[position()=2]"
             ))).click()
def drop_off_location(dropoff_location_str):
    """Drop off location"""
    # Locate the input element by its ID
    pickup_location_input = driver.find_element(By.ID, 'DropoffLocation')

    # Set the input value
    pickup_location_input.clear()  # Clear the input field first, if necessary
    pickup_location_input.send_keys(dropoff_location_str)

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//div[@id='DropoffLocationSuggestionDiv']/ul//li[position()=2]"
             ))).click()

# --------------------------------------------------
def main():
    args = get_args()
    url_str = args.url
    service_type = args.service_type
    date_str = args.date
    time_str = args.time
    pickup_location_str = args.pickup_location_str
    dropoff_location_str = args.dropoff_location_str

    try:
        driver.maximize_window()
        driver.get(url_str)

        # using this because of poor connection
        time.sleep(10)
        switch_to_frame()

        if service_type == 1:
            """if service type is to airport"""
            select_service(service_type)
            select_date(date_str)
            select_time(time_str)
            pickUp_location(pickup_location_str)
            drop_off_location(dropoff_location_str)

    except Exception as ex:
        print(ex)

    finally:
        time.sleep(5)
        driver.close()
        driver.quit()

# --------------------------------------------------
if __name__ == '__main__':
    main()
