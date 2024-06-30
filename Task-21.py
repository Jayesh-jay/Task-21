from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Step 1: Open the URL
driver.get("https://www.saucedemo.com/")

# Step 2: Log in
username = "standard_user"
password = "secret_sauce"
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

# Wait for the page to load after login
time.sleep(3)

# Step 3: Display cookies
cookies = driver.get_cookies()
print("Cookies after login:")
for cookie in cookies:
    print(f"{cookie['name']}: {cookie['value']}")

# Step 4: Access the dashboard

# Step 5: Log out
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "logout_sidebar_link").click()

# Wait for the page to load after logout
time.sleep(3)

# Step 6: Verify cookies after logout
cookies_after_logout = driver.get_cookies()
print("\nCookies after logout:")
for cookie in cookies_after_logout:
    print(f"{cookie['name']}: {cookie['value']}")

# Close the browser window
driver.quit()
