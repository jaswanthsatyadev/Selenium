#TOPICS
#XPath


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://qapodcastpage.ccbp.tech/"

#setup
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)

