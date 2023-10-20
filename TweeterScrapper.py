from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pypyodbc as odbc

#Base de Datos
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'LAPTOP-KPJGE02C'
DATABASE_NAME = 'TweeterScrapper'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
cursor = conn.cursor()

#Selenium
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver.get("https://twitter.com/hashtag/LivingIbrp?src=hashtag_click")

time.sleep(5)

#Programa
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

    sql = """
    INSERT INTO Data (Usuario, AtUsuario, Tweet, Foto, FotoPerfil) VALUES (?, ?, ?, ?, ?)
    """
    data = []


    try:
        tweetUsers = tweet.find_element(By.CSS_SELECTOR, '[data-testid="User-Name"] [role="link"]')
    except:
        print("No hay mas tweets")
        quit()
    else:
        data.append(tweetUsers.text)

    tweetAt = tweet.find_element(By.CSS_SELECTOR, '[data-testid="User-Name"] [tabindex="-1"]')
    data.append(tweetAt.text)

    tweetTexts = tweet.find_element(By.CSS_SELECTOR, '[data-testid="tweetText"]')
    data.append(" ".join(tweetTexts.text.split()))

    try:
        tweetFotos = tweet.find_element(By.CSS_SELECTOR, '[data-testid="tweetPhoto"] img')
    except:
        data.append("NULL")
    else:
        data.append(tweetFotos.get_attribute("src"))

    tweetFotoPerfil = tweet.find_element(By.CSS_SELECTOR, '[data-testid="Tweet-User-Avatar"] img')
    data.append(tweetFotoPerfil.get_attribute("src"))
    print(data)

    cursor.execute(sql, data)
    conn.commit()

conn.close()


# for tweet in tweets:
#
#     id = 1
#
#     try:
#         tweetUsers = tweet.find_element(By.CSS_SELECTOR, '[data-testid="User-Name"] [role="link"]')
#     except:
#         print("No hay mas tweets")
#         quit()
#     else:
#         cursor.execute(f'''
#             UPDATE Data
#             SET Usuario = {tweetUsers.text}
#             WHERE ID = {id}
#         ''')
#         Db.conn.commit
#
#     tweetAt = tweet.find_element(By.CSS_SELECTOR, '[data-testid="User-Name"] [tabindex="-1"]')
#     cursor.execute(f'''
#         UPDATE Data
#         SET AtUsuario = {tweetAt.text}
#         WHERE ID = {id}
#     ''')
#     Db.conn.commit
#
#     tweetTexts = tweet.find_element(By.CSS_SELECTOR, '[data-testid="tweetText"]')
#     cursor.execute(f'''
#         UPDATE Data
#         SET Tweet = {" ".join(tweetTexts.text.split())}
#         WHERE ID = {id}
#     ''')
#     Db.conn.commit
#     #print("Tweet:" + " ".join(tweetTexts.text.split()))
#
#     try:
#         tweetFotos = tweet.find_element(By.CSS_SELECTOR, '[data-testid="tweetPhoto"] img')
#     except:
#         print("No hay foto adjunta")
#     else:
#         cursor.execute(f'''
#             UPDATE Data
#             SET Foto = {tweetFotos.get_attribute("src")}
#             WHERE ID = {id}
#         ''')
#         Db.conn.commit
#         #print("Foto:" + tweetFotos.get_attribute("src"))
#
#     tweetFotoPerfil = tweet.find_element(By.CSS_SELECTOR, '[data-testid="Tweet-User-Avatar"] img')
#     cursor.execute(f'''
#                 UPDATE Data
#                 SET FotoPerfil = {tweetFotoPerfil.get_attribute("src")}
#                 WHERE ID = {id}
#             ''')
#     Db.conn.commit
#     ##print("FotoPerfil:" + tweetFotoPerfil.get_attribute("src"))
#     id + 1

#aria-label="Cronología: Buscar en la cronología"
#data-testid="cellInnerDiv"
#data-testid="tweet"
#data-testid="Tweet-User-Avatar" (Buscar dentro de aca el tag img)
#data-testid="User-Name"
#data-testid="tweetText"
#data-testid="tweetPhoto"


