from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException,StaleElementReferenceException
import os

from bs4 import BeautifulSoup

import time

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
#use to change the webdriver wait times
Wait = WebDriverWait(driver, 30)
#adjust this based on connection speed


def switch_to_frame():
    Wait.until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, 'iFrameResizer0'))
    )
    # driver.switch_to.frame(iframe)
    
#select service type
def select_service():
    #wait for the precense of element to be located
    Wait.until(
        EC.presence_of_element_located((By.ID, 'ServiceTypeId'))
        
    )

    # Locate the drop-down menu to select the location
    # Replace with the actual ID of the drop-down
    dropdown_element = driver.find_element(By.ID, 'ServiceTypeId')

    # Creating a Select object
    select = Select(dropdown_element)

    #select by index (0-based index)
    select.select_by_index(1)



    #Locate the date input field by its ID

    # wait for the prescence of an element if what what we're looking for doesn't exist yet
    
    
def select_date():
    """select the appropriate time"""
    Wait.until(
        EC.presence_of_element_located((By.ID, 'PickUpDate'))
        
    )

    date_input = driver.find_element(By.ID, 'PickUpDate')
    date_input.click()
    date_input.clear()

    #python way of find date and inputing 
    # calendar_table = driver.find_element(By.CLASS_NAME, "table-condensed")

    # xpath_day = '//td[@class="day" and text()="23"]'

    # calendar_day = driver.find_element(By.XPATH, xpath_day)
    # calendar_day.click()

    # outside_element = driver.find_element(By.ID, "PickupLocationLabel")
    # outside_element.click()
    
    # Optionally, you can use JavaScript to set the date if direct input doesn't work
    driver.execute_script("arguments[0].value = '06/30/2024';", date_input)
       
def select_time():
    
    # Locate the input element by its ID
    time_input = driver.find_element(By.ID, 'PickUpTime')

    # Set the time value
    # Clear the field first (if necessary)
    time_input.clear()
    
    # # Enter the desired time in the format expected by the input field
    # time_input.send_keys('10:30 AM')  # Replace with your desired time format

    # Optionally, you can use JavaScript to set the time if direct input doesn't work
    driver.execute_script("arguments[0].value = '10:30 AM';", time_input)

    
def pickUp_location():
    # Locate the input element by its ID
    pickup_location_input = driver.find_element(By.ID, 'PickupLocation')

    # Set the input value
    pickup_location_input.clear()  # Clear the input field first, if necessary
    pickup_location_input.send_keys('ATL Airport')

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='PickupLocationSuggestionDiv']/ul//li[position()=2]"))
    ).click()
    

def drop_off_location():
        # Locate the input element by its ID
    pickup_location_input = driver.find_element(By.ID, 'DropoffLocation')

    # Set the input value
    pickup_location_input.clear()  # Clear the input field first, if necessary
    pickup_location_input.send_keys('sandy springs')
    
    Wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='DropoffLocationSuggestionDiv']/ul//li[position()=2]"))
    ).click()


def add_stop():
    # Locate the <a> element by its ID
    add_stop_link = driver.find_element(By.ID, 'addNewStopLink')

    # Click the element
    add_stop_link.click()
    
    # after clicking add a stop link
    # Locate the input element by its ID
    stop_input = driver.find_element(By.ID, 'Stops_1_')

    #Set the input value
    stop_input.clear()  # Clear the input field first, if necessary
    stop_input.send_keys('BMW')  # Replace with your desired stop location
    
    Wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='Stops_1_SuggestionDiv']/ul//li[position()=1]"))
    ).click()

def no_passengers():

    # Locate the input element by its ID
    passenger_input = driver.find_element(By.ID, 'PassengerNumber')

    # Set the number value
    # Clear the field first (if necessary)
    passenger_input.clear()
    
    # # Enter the desired number of passengers
    # passenger_input.send_keys('4')  # Replace with your desired number

    # Optionally, you can use JavaScript to set the number if direct input doesn't work
    driver.execute_script("arguments[0].value = '1';", passenger_input)


def luggage_count():

    # Locate the input element by its ID
    luggage_input = driver.find_element(By.ID, 'LuggageCount')

    #Set the number value
    # Clear the field first (if necessary)
    luggage_input.clear()
    
    # # Enter the desired luggage count
    # luggage_input.send_keys('3')  # Replace with your desired number

    # Optionally, you can use JavaScript to set the number if direct input doesn't work
    driver.execute_script("arguments[0].value = '3';", luggage_input)


def select_vehicle():
    # Locate and click select vehicle by its ID
    Wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='showRatesBtn']"))
    ).click()

def save_page_source(filename):
    # """create the data folder if it doesnt exist"""
    if not os.path.exists('data'):
        os.makedirs('data')
        
    """Save the current page source to a file in the data folder."""
    with open(os.path.join('data', filename), 'w', encoding='utf-8') as file:
        file.write(driver.page_source)
          
        
def click_next_until_disabled():

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
            
            # Wait for the current page button to be clickable
            page_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(pages[page_num])
            )

            # Click the page button
            page_button.click()
            print(f"Clicked page {page_num + 1}")
        except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException) as e:
            print("No longer clickable or not found:", e)
            break
        except Exception as e:
            print("An unexpected error occurred:", e)
            break



def get_html(url):
    """Getting the webiste """
    try:
        driver.maximize_window()
        driver.get(url)
        
        #using this because of poor connection
        time.sleep(10)
       
        switch_to_frame()
        select_service()
        select_date()
        select_time()
        pickUp_location()
        #add_stop()
        drop_off_location()
        no_passengers()
        luggage_count()
        select_vehicle()
        click_next_until_disabled()


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_html("https://www.mayslimo.com/online-booking/")


if __name__ == "__main__":
    main()