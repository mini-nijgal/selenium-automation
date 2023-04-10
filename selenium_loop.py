import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import traceback
import logging



# Read email addresses from CSV file

emails = []
with open("C:/Users/mini/OneDrive/Desktop/Email.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        emails.append(row[0])

# Initialize web driver with pop-up blocking options
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the page
browser.get("URL")
browser.maximize_window()

for email in emails:
    try:
        # Find the email input field and enter email
        email_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'pl')))
        email_input.clear()  # Clear any existing text in the email input field
        email_input.send_keys(email)
        print(f"Email '{email}' added successfully")

        # Find the checkbox and click on it
        checkbox = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'newnewsletter')))
        browser.execute_script("arguments[0].click();", checkbox)

        print("Checkbox was clicked")
        # Find the submit button and click on it
        button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Sign me up")]')))
        browser.execute_script("arguments[0].click();", button)
        print ("button was clicked")
        browser.execute_script("window.stop();")

        WebDriverWait(browser, 10)

    except Exception as e:
        logging.error(traceback.format_exc())
