from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import yt_dlp

# Prompt user for Instagram credentials and hashtag
username = input("Enter Instagram username: ")
password = input("Enter Instagram password: ")
tag = input("Enter Instagram hashtag (without #): ")

# Start Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

driver.get("https://www.instagram.com/accounts/login/")

# Wait for login fields to appear
wait = WebDriverWait(driver, 20)
try:
    username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
except Exception as e:
    print(f"Login fields not found: {e}")
    driver.quit()
    exit(1)

# Enter credentials and log in
username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

# Go to hashtag page
driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
time.sleep(5)

# Scroll to load more posts
for _ in range(2):  # Increase range for more posts
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(3)

# Extract post and reel links
links = set()
elems = driver.find_elements(By.TAG_NAME, 'a')
for elem in elems:
    href = elem.get_attribute("href")
    if href and ('/p/' in href or '/reel/' in href):
        links.add(href)

print("Post links:")
links_list = list(links)
for link in links_list:
    print(link)

driver.quit()

ydl_opts = {
    'outtmpl': '%(title)s_%(id)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',
    'ignoreerrors': True,
    'download_archive': 'downloaded.txt'  # Optional but recommended
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links_list)

