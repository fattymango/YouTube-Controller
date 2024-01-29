from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.chrome.service import Service
chromedriver_binary.add_chromedriver_to_path()
print(chromedriver_binary.chromedriver_filename)
driver = webdriver.Chrome(service=Service(executable_path="C:\\Users\\malak\\Desktop\\Projects\\Python\\ytp-controller\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe"))
driver.get("http://www.python.org")