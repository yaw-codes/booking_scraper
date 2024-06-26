from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, TimeoutException
import os
import time

# Initialize WebDriver
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30)


def switch_to_frame():
    """Switch to the iframe containing the booking form."""
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'iFrameResizer0')))


def select_service():
    """Select the service type from the dropdown."""
    wait.until(EC.presence_of_element_located((By.ID, 'ServiceTypeId')))
    dropdown_element = driver.find_element(By.ID, 'ServiceTypeId')
    select = Select(dropdown_element)
    select.select_by_index(1)


def select_date():
    """Select the pickup date."""
    wait.until(EC.presence_of_element_located((By.ID, 'PickUpDate')))
    date_input = driver.find_element(By.ID, 'PickUpDate')
    date_input.clear()
    driver.execute_script("arguments[0].value = '06/30/2024';", date_input)


def select_time():
    """Select the pickup time."""
    time_input = driver.find_element(By.ID, 'PickUpTime')
    time_input.clear()
    driver.execute_script("arguments[0].value = '10:30 AM';", time_input)


def pick_up_location():
    """Set the pickup location."""
    pickup_location_input = driver.find_element(By.ID, 'PickupLocation')
    pickup_location_input.clear()
    pickup_location_input.send_keys('ATL Airport')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='PickupLocationSuggestionDiv']/ul//li[position()=2]"))).click()


def drop_off_location():
    """Set the drop-off location."""
    dropoff_location_input = driver.find_element(By.ID, 'DropoffLocation')
    dropoff_location_input.clear()
    dropoff_location_input.send_keys('Sandy Springs')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='DropoffLocationSuggestionDiv']/ul//li[position()=2]"))).click()


def no_passengers():
    """Set the number of passengers."""
    passenger_input = driver.find_element(By.ID, 'PassengerNumber')
    passenger_input.clear()
    driver.execute_script("arguments[0].value = '1';", passenger_input)


def luggage_count():
    """Set the luggage count."""
    luggage_input = driver.find_element(By.ID, 'LuggageCount')
    luggage_input.clear()
    driver.execute_script("arguments[0].value = '3';", luggage_input)


def select_vehicle():
    """Select the vehicle."""
    wait.until(EC.element_to_be_clickable((By.ID, "showRatesBtn"))).click()


def click_rate_details_buttons():
    """Click the rate details button for each vehicle item."""
    try:
        vehicle_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "vehicle-item-class-name")))
        for vehicle_item in vehicle_items:
            try:
                button = vehicle_item.find_element(By.CLASS_NAME, "vehicle-decription-btn")
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                button.click()
            except Exception as e:
                print(f"Could not click the button for a vehicle item: {e}")
    except Exception as e:
        print(f"An error occurred while trying to click rate details buttons: {e}")


def save_page_source(filename):
    """Save the current page source to a file in the data folder."""
    if not os.path.exists('data'):
        os.makedirs('data')
    with open(os.path.join('data', filename), 'w', encoding='utf-8') as file:
        file.write(driver.page_source)


def click_next_until_disabled():
    """Click through pagination until the next button is disabled."""
    pages = driver.find_elements(By.CSS_SELECTOR, 'li.page a')
    num_pages = len(pages)
    for page_num in range(num_pages):
        try:
            pages = driver.find_elements(By.CSS_SELECTOR, 'li.page a')
            time.sleep(10)
            save_page_source(f'page_{page_num}.html')
            page_button = wait.until(EC.element_to_be_clickable(pages[page_num]))
            page_button.click()
            print(f"Clicked page {page_num + 1}")
        except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException) as e:
            print("No longer clickable or not found:", e)
            break
        except Exception as e:
            print("An unexpected error occurred:", e)
            break


def get_html(url):
    """Main function to perform all interactions on the website."""
    try:
        driver.maximize_window()
        driver.get(url)
        time.sleep(20)
        switch_to_frame()
        select_service()
        select_date()
        select_time()
        pick_up_location()
        drop_off_location()
        no_passengers()
        luggage_count()
        select_vehicle()
        click_rate_details_buttons()
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
