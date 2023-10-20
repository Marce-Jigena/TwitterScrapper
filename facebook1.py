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
user = "TTest24569213"

userEmail = driver.find_element(By.CSS_SELECTOR, '[name="text"]')
userEmail.send_keys(email)
driver.find_element(By.CSS_SELECTOR, '[class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]').click()

time.sleep(3)

boton = driver.find_element(By.CSS_SELECTOR, '[aria-disabled="true"]')
userName = driver.find_element(By.CSS_SELECTOR, '[name="text"]')
userName.send_keys(user)
boton.click()

time.sleep(3)

password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
password.send_keys(userPassword)
driver.find_element(By.CSS_SELECTOR, '[data-testid="LoginForm_Login_Button"]').click()


time.sleep(15)

tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
for tweet in tweets:
    try:
        tweetUsers = tweet.find_element(By.CSS_SELECTOR, '[data-testid="User-Name"] [role="link"]')
    except:
        print("No hay mas tweets")
        quit()
    else:
        print("Usuario:" + tweetUsers.text)
    tweetAt = tweet.find_element(By.CSS_SELECTOR, '[data-testid="User-Name"] [tabindex="-1"]')
    print("@:" + tweetAt.text)
    tweetTexts = tweet.find_element(By.CSS_SELECTOR, '[data-testid="tweetText"]')
    print("Tweet:" + tweetTexts.text)
    try:
        tweetFotos = tweet.find_element(By.CSS_SELECTOR, '[data-testid="tweetPhoto"] img')
    except:
        print("No hay foto adjunta")
    else:
        print("Foto:" + tweetFotos.get_attribute("src"))
    tweetFotoPerfil = tweet.find_element(By.CSS_SELECTOR, '[data-testid="Tweet-User-Avatar"] img')
    print("FotoPerfil:" + tweetFotoPerfil.get_attribute("src"))


#aria-label="Cronología: Buscar en la cronología"
#data-testid="cellInnerDiv"
#data-testid="tweet"
#data-testid="Tweet-User-Avatar" (Buscar dentro de aca el tag img)
#data-testid="User-Name"
#data-testid="tweetText"
#data-testid="tweetPhoto"


