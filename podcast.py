#TOPICS
#XPath

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
browser = webdriver.Chrome()
browser.get("https://qapodcastpage.ccbp.tech/")
time.sleep(2)

# Find list of podcast items
podcast_cards = browser.find_elements(By.XPATH, "//div[@class='details-card']")

# Iterating through each podcast item
for podcast in podcast_cards:
    
    podcast.click()
    time.sleep(2)

    # Find all episodes for the selected podcast
    episode_containers = browser.find_elements(By.XPATH, "//div[@class='podcast-episode-container']")
    
    if len(episode_containers) == 4:
        print("All 4 Episodes Found.")

    else:
        print(f"Only {len(episode_containers)}  Episodes Found.")

    # go back to home page
    back_button = browser.find_element(By.XPATH, "//button[contains(text(),'Back')]")
    back_button.click()
    time.sleep(2)

time.sleep(5)   