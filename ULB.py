import time
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Elemente aus der Datenbank die gebraucht werden
Benutzername = "jfrick1"
Passwort = "JuliusClemens2002"
Ulbnummer = "A25241981/2"

#Einstellungen
service_object_name = Service(r'/Users/juliusfrick/Documents/Programmieren/Selenium/chromedriver')
options_name = webdriver.ChromeOptions()
options_name.add_argument("--start-maximized")
options_name.add_experimental_option("excludeSwitches", ["enable-automation"])
options_name.add_experimental_option('useAutomationExtension', False)
options_name.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=service_object_name, options=options_name)


#Aufrufen der Website
driver.get("https://sso.uni-muenster.de/ULB/sso/wwu/platzreservierung/")

#Anmelden bei WWU-SSO
wwu_benutzer = driver.find_element(by=By.ID, value = "httpd_username").send_keys(Benutzername)
wwu_passwort = driver.find_element(by=By.ID, value = "httpd_password").send_keys(Passwort)
wwu_button = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/section[2]/article[1]/div/form/p/input[4]").click()


#Ist nur hier um Fehler zu vermeiden
time.sleep(2)



#Macht das Capchta
captcha = driver.find_element(by=By.XPATH, value="/html/body/main/div/div/section/div/div/form/div[3]/img").screenshot('captcha.png')
image = Image.open('captcha.png')
text = pytesseract.image_to_string(image)
#print(text)
captcha_text = driver.find_element(by=By.ID, value="captcha").click()
captcha_text = driver.find_element(by=By.ID, value="captcha").send_keys(text)


#Eintragen Auf der Registrierungswebiste
#ulb_nummer = driver.find_element(by=By.ID, value="benutzernummer").send_keys(Ulbnummer)
#datenschutz = driver.find_element(by=By.ID, value="datenschutzerklaerung_akzeptiert").click()








#captcha_button = driver.find_element(by=By.CLASS_NAME, value="ym-button ym-next ym-success").click()

time.sleep(1000)
