import os
from bs4 import BeautifulSoup

# Directory containing the HTML files
directory = 'data'  # Replace with the path to your HTML files directory

# Function to parse an HTML file
def parse_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'lxml')
        
    # Extract addresses
    addresses = []
    for p in soup.find_all('p'):
        if p.find('svg', class_='svg-icon svg-location'):
            address = p.get_text(strip=True)  # Extract and strip text from <p>
            addresses.append(address)
    
    # Extract date and time
    date_time = 'NA'
    date_time_element = soup.find('div', class_='step-info-date')
    if date_time_element:
        date_time = date_time_element.find('h6').text.strip()

    # Extract data for each vehicle grid item
    vehicles = []
    for vehicle_item in soup.find_all('div', class_='vehicle-grid-item'):
        # Get vehicle type
        vehicle_type = vehicle_item.find('h2', class_='vehicle-grid-item-heading').text.strip()

        # Get vehicle model (from description)
        model_description_container = vehicle_item.find('div', id=lambda x: x and x.startswith('vehicleDescription'))
        if model_description_container:
            vehicle_model = model_description_container.find('p').text.strip()
        else:
            vehicle_model = 'NA'  # Not Available

        # Get price
        price_container = vehicle_item.find('div', class_='vehicle-grid-item-price-numb')
        price = price_container.get_text().strip() if price_container else 'NA'
        
        # Get number of passengers & luggage
        pass_container = vehicle_item.find_all('span', class_='input-group-addon')
        pass_no = pass_container[1].text.strip() if len(pass_container) > 1 else 'NA'
        lag_no = pass_container[3].text.strip() if len(pass_container) > 3 else 'NA'

        # Add data to dictionary and append to vehicles list
        vehicle_data = {
            'Vehicle Type': vehicle_type,
            'Vehicle Model': vehicle_model,
            'Price': price,
            'Passenger No.': pass_no,
            'Luggage No': lag_no,
            'Date & Time': date_time,
        }
        
        # Check if there are addresses and assign them
        if len(addresses) > 0:
            vehicle_data['Pick-Up Location'] = addresses[0]
        if len(addresses) > 1:
            vehicle_data['Drop-Off Location'] = addresses[1]

        vehicles.append(vehicle_data)

    # Print data in a tabular format
    print(" | ".join(['Vehicle Type', 'Vehicle Model', 'Price', 'Passenger No.', 'Luggage No', 'Date & Time', 'Pick-Up Location', 'Drop-Off Location']))
    print("-" * 100)
    for vehicle in vehicles:
        print(" | ".join([vehicle.get(key, 'NA') for key in ['Vehicle Type', 'Vehicle Model', 'Price', 'Passenger No.', 'Luggage No', 'Date & Time', 'Pick-Up Location', 'Drop-Off Location']]))

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):  # Process only HTML files
        file_path = os.path.join(directory, filename)
        parse_html_file(file_path)
