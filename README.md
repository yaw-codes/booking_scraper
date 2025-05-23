# 🏨 Booking Scraper

A Python-based web scraper designed to extract and compare limo prices from various limo sites

---

## 📌 Features

* Scrapes vehicle Prices listings from various limo sites
* Parses and processes HTML content using BeautifulSoup
* Stores extracted data into a PostgreSQL database
* Includes multiple scripts for data extraction, processing, and storage
* Provides Jupyter notebooks for testing and demonstration purposes

---

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yaw-codes/booking_scraper.git
   cd booking_scraper
   ```



2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```



4. **Set up the PostgreSQL database:**

   * Ensure PostgreSQL is installed and running.

   * Create a new database:

     ```bash
     createdb booking_data
     ```

   * Run the provided SQL script to set up the necessary tables:([GitHub][1])

     ```bash
     psql -d booking_data -f schema_table.sql
     ```

---

## 🚀 Usage

### 1. **Scraping Data**

Use the `booking_stream.py` script to initiate the scraping process

```bash
python booking_stream.py
```



### 2. **Processing and Storing Data**

After scraping, process and store the data into PostgreSQL using:

```bash
python soup_postgres_store.py
```



### 3. **Testing and Exploration**

Explore the data and test functionalities using the provided Jupyter notebooks:

* `soup_test_note.ipynb`
* `test_booking_scprt.ipynb`

Launch Jupyter Notebook:

```bash
jupyter notebook
```



---

## 📁 Project Structure

```plaintext
booking_scraper/
├── booking_stream.py             # Main script to scrape booking data
├── soup_postgres_store.py        # Processes and stores data into PostgreSQL
├── schema_table.sql              # SQL schema for PostgreSQL database
├── soup_test_note.ipynb          # Jupyter notebook for testing
├── test_booking_scprt.ipynb      # Additional testing notebook
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── ...                           # Other auxiliary scripts and files
```

---

## 📦 Dependencies

Ensure the following Python packages are installed (handled via `requirements.txt`):

* `requests`
* `beautifulsoup4`
* `selenium`
* `psycopg2`
* `pandas`
* `jupyterlab`

---

## ⚠️ Disclaimer

This project is intended for educational and personal use only. Scraping data from websites may violate their terms of service. Ensure you have permission to scrape data and use it responsibly.
