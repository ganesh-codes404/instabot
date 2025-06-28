from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "your_dummy_username"
PASSWORD = "your_dummy_password"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.instagram.com/")

    time.sleep(3)
    try:
        driver.find_element(By.XPATH, "//button[text()='Only allow essential cookies']").click()
        time.sleep(2)
    except:
        pass

    # Enter login details
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)

    time.sleep(5)

    # Search for 'cbitosc'
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_input.send_keys("cbitosc")
    time.sleep(2)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)
    search_input.send_keys(Keys.ENTER)

    time.sleep(5)

    # Follow the account
    try:
        follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
        follow_button.click()
        print("Followed the account.")
    except:
        print("Already following or button not found.")

    time.sleep(3)

    # Extract profile data
    bio = driver.find_element(By.XPATH, "//div[@class='_aa_c']//div[@class='_aacl _aacp _aacw _aacx _aad7 _aade']").text
    stats = driver.find_elements(By.XPATH, "//ul[@class='_ac2a']/li")

    posts = stats[0].text
    followers = stats[1].text
    following = stats[2].text

    profile_data = f"""
CBIT OSC Instagram Profile Data:

Bio: {bio}
Posts: {posts}
Followers: {followers}
Following: {following}
"""

    print(profile_data)

    # Save to file
    with open("profile_data.txt", "w", encoding="utf-8") as f:
        f.write(profile_data)

finally:
    time.sleep(5)
    driver.quit()
