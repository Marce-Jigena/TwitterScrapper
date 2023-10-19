from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver.get("https://twitter.com/hashtag/LivingIbrp?src=hashtag_click")

time.sleep(5)

email = "TweetTest245@proton.me"
userPassword = "TweetTest"

username = driver.find_element(By.CSS_SELECTOR, '[name="text"]')

print(username)