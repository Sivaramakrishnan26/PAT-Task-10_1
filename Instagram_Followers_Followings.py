from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the chrome webdriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open a website
driver.get("https://www.instagram.com/guviofficial/")

# Wait for the page to load
time.sleep(10)

# Initialize the WebDriverWait
wait = WebDriverWait(driver, 10)

# Try to locate and print the number of Followers and Followings
try:
    Followers = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='171K']/span")))
    print(f"Followers: {Followers.text}")
    
    Followings = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='5']/span")))
    print(f"Followings: {Followings.text}")

except Exception as e:
    print(f"Error: {e}")               

# Close the WebDriver
driver.quit()