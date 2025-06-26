# TOPICS

# PIP
# Selenium WebDriver
# ChromeDriver setup 
# Waits (implicit/explicit)
# By

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://qaflightbooking.ccbp.tech/"

#setup
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)

#locators
departure_city_field = driver.find_element(By.ID, "departureCity")
destination_city_field = driver.find_element(By.ID, "destinationCity")
travel_date_field = driver.find_element(By.ID, "travelDate")
passengers_field = driver.find_element(By.ID, "passengers")
search_btn = driver.find_element(By.ID, "searchBtn")

#values
departure_city_field.send_keys("New York")
destination_city_field.send_keys("Los Angeles")
travel_date_field.send_keys("01/08/2023")
passengers_field.send_keys("2")


#search
time.sleep(2)
search_btn.click()

#airlines
airlines = driver.find_element(By.NAME, "flight")
airlines.click()

#book now
time.sleep(3)
booknow_btn = driver.find_element(By.TAG_NAME, "button" )
booknow_btn.click()

#wallet balance
wallet_balance = driver.find_element(By.TAG_NAME, "p")
print(wallet_balance.text)

#payment
password = driver.find_element(By.TAG_NAME, "input")
password.send_keys("traveler123")
pay_btn = driver.find_element(By.TAG_NAME, "button")
pay_btn.click()

#success page
time.sleep(2)
page_heading = driver.find_element(By.TAG_NAME, "h2")
print(page_heading.text)


#quit
driver.quit()