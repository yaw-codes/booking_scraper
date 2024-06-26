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

    parser.add_argument('-stop',
                        '--add_stop',
                        help='boolean flag to add stop',
                        action='store_true')
    parser.add_argument('-pn',
                        '--pass_num',
                        help='no of passengers int',
                        metavar='int',
                        type=int,
                        default=1)
    parser.add_argument('-nh',
                        '--hr_num',
                        help='no of hours int',
                        metavar='int',
                        type=int)

    parser.add_argument('-lc',
                        '--luggage_num',
                        help='count of luggage int',
                        metavar='int',
                        type=int,
                        default=1)
    parser.add_argument('-rl',
                        '--bool_rtn_loc',
                        help='boolean flag to add stop',
                        action='store_true')

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


def add_stop(bool_stop):
    """checks to see whether we need stops"""
    if bool_stop:
        # Locate the <a> element by its ID
        add_stop_link = driver.find_element(By.ID, 'addNewStopLink')

        # Click the element
        add_stop_link.click()

        # after clicking add a stop link
        # Locate the input element by its ID
        stop_input = driver.find_element(By.ID, 'Stops_1_')

        # Set the input value
        stop_input.clear()  # Clear the input field first, if necessary
        stop_input.send_keys('BMW')  # Replace with your desired stop location

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//div[@id='Stops_1_SuggestionDiv']/ul//li[position()=1]"
                 ))).click()


def no_passengers(pass_num):
    """Passanger number"""

    # Locate the input element by its ID
    passenger_input = driver.find_element(By.ID, 'PassengerNumber')

    # Set the number value
    # Clear the field first (if necessary)
    passenger_input.clear()

    # # Enter the desired number of passengers
    # passenger_input.send_keys('4')  # Replace with your desired number

    # Optionally, you can use JavaScript to set the number if direct input doesn't work
    driver.execute_script(f"arguments[0].value = '{pass_num}';",
                          passenger_input)


def no_hours(hr_num):
    """estimated duration of trip"""

    # Locate the input element by its ID
    no_hours = driver.find_element(By.ID, 'HoursNumber')

    # Set the number value
    # Clear the field first (if necessary)
    no_hours.clear()

    # # Enter the desired number of passengers
    # passenger_input.send_keys('4')  # Replace with your desired number

    # Optionally, you can use JavaScript to set the number if direct input doesn't work
    driver.execute_script(f"arguments[0].value = '{hr_num}';", no_hours)


def luggage_count(luggage_num):
    """Estimated number of luggage """

    # Locate the input element by its ID
    luggage_input = driver.find_element(By.ID, 'LuggageCount')

    # Set the number value
    # Clear the field first (if necessary)
    luggage_input.clear()

    # # Enter the desired luggage count
    # luggage_input.send_keys('3')  # Replace with your desired number

    # Optionally, you can use JavaScript to set the number if direct input doesn't work
    driver.execute_script(f"arguments[0].value = '{luggage_num}';",
                          luggage_input)


def return_at_diff_location(bool_rtn_loc):
    """clicks the return to diff location checkbox"""
    if bool_rtn_loc:
        # Locate the checkbox using its ID
        checkbox = driver.find_element(By.ID, 'showDropoffLocation')

        # Scroll to the checkbox if necessary (sometimes required for elements not in view)
        ActionChains(driver).move_to_element(checkbox).perform()

        # Click the checkbox to check it
        checkbox.click()

        # # Optional: Verify if the checkbox is selected
        # is_selected = checkbox.is_selected()
        # print(f"Checkbox selected: {is_selected}")


def select_vehicle():
    """clicks the select vechicle button"""
    # Locate and click select vehicle by its ID
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='showRatesBtn']"))).click()


def click_rate_details_buttons():
    """Click the rate details button for each vehicle item."""
    #first implementation
    # try:
    #     vehicle_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "vehicle-grid-item-price")))
    #     for vehicle_item in vehicle_items:
    #         try:
    #             button = vehicle_item.find_element(By.CLASS_NAME, "vehicle-decription-btn")
    #             driver.execute_script("arguments[0].scrollIntoView(true);", button)
    #             button.click()
    #         except Exception as e:
    #             print(f"Could not click the button for a vehicle item: {e}")
    # except Exception as e:
    #     print(f"An error occurred while trying to click rate details buttons: {e}")

    #second implementation
    try:
        vehicle_items = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "vehicle-grid-item-price")))
        for vehicle_item in vehicle_items:
            try:
                #there are two vehicle description buttons in the vehicle item .. we need to select the second one
                buttons = vehicle_item.find_elements(By.CLASS_NAME,
                                                     "vehicle-decription-btn")
                # Scroll to the button to make sure it is in view (optional, depending on the page layout)
                ActionChains(driver).move_to_element(price_button).perform()
                price_button = buttons[1]
                price_button.click()
            except Exception as e:
                print(f"Could not click the button for a vehicle item: {e}")
    except Exception as e:
        print(
            f"An error occurred while trying to click rate details buttons: {e}"
        )


def save_page_source(filename):
    """create the data folder if it doesnt exist"""
    if not os.path.exists('data'):
        os.makedirs('data')
    """Save the current page source to a file in the data folder."""
    with open(os.path.join('data', filename), 'w', encoding='utf-8') as file:
        file.write(driver.page_source)


def click_next_until_disabled():
    """cleck the next page button"""
    pages = driver.find_elements(By.CSS_SELECTOR, 'li.page a')
    num_pages = len(pages)

    for page_num in range(num_pages):
        try:

            # Re-find all page elements to avoid stale element reference
            pages = driver.find_elements(By.CSS_SELECTOR, 'li.page a')

            # Adding a sleep time to ensure the webpage fully loads
            time.sleep(10)

            # Save the current page source
            save_page_source(f'page_{page_num}.html')

            #click rate buttons
            click_rate_details_buttons()

            # wait for the current page button to be clickable
            page_button = wait.until(
                EC.element_to_be_clickable(pages[page_num]))

            # Click the page button
            page_button.click()
            print(f"Clicked page {page_num + 1}")
        except (NoSuchElementException, ElementClickInterceptedException,
                StaleElementReferenceException) as e:
            print("No longer clickable or not found:", e)
            break
        except Exception as e:
            print("An unexpected error occurred:", e)
            break


# --------------------------------------------------
def main():
    args = get_args()
    url_str = args.url
    service_type = args.service_type
    date_str = args.date
    time_str = args.time
    pickup_location_str = args.pickup_location_str
    dropoff_location_str = args.dropoff_location_str
    bool_stop = args.add_stop
    pass_num = args.pass_num
    hr_num = args.hr_num
    luggage_num = args.luggage_num
    bool_rtn_loc = args.bool_rtn_loc

    try:
        driver.maximize_window()
        driver.get(url_str)

        # using this because of poor connection
        time.sleep(10)
        switch_to_frame()

        if service_type == 0:
            """if service type is from airport"""
            select_service(service_type)
            select_date(date_str)
            select_time(time_str)
            pickUp_location(pickup_location_str)
            drop_off_location(dropoff_location_str)
            no_passengers(pass_num)
            luggage_count(luggage_num)
            select_vehicle()
            click_next_until_disabled()

        elif service_type == 1:
            """if service type is from airport"""
            select_service(service_type)
            select_date(date_str)
            select_time(time_str)
            pickUp_location(pickup_location_str)
            drop_off_location(dropoff_location_str)
            no_passengers(pass_num)
            luggage_count(luggage_num)
            select_vehicle()
            click_next_until_disabled()

        elif service_type == 2:
            """if service type is point to point"""
            select_service(service_type)
            select_date(date_str)
            select_time(time_str)
            pickUp_location(pickup_location_str)
            drop_off_location(dropoff_location_str)
            no_passengers(pass_num)
            luggage_count(luggage_num)
            select_vehicle()
            click_next_until_disabled()

        elif service_type == 3:
            """if service type is hourly"""
            select_service(service_type)
            select_date(date_str)
            select_time(time_str)
            pickUp_location(pickup_location_str)
            drop_off_location(dropoff_location_str)
            no_passengers(pass_num)
            luggage_count(luggage_num)
            select_vehicle()
            click_next_until_disabled()
        

    except Exception as ex:
        print(ex)

    finally:
        time.sleep(5)
        driver.close()
        driver.quit()


# --------------------------------------------------
if __name__ == '__main__':
    main()
