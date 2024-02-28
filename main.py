from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialiser le navigateur
driver = webdriver.Chrome()

# Ouvrir le site d'actualités/de commerce
driver.get("https://example.com")

# Effectuer une recherche
search_box = driver.find_element(By.CSS_SELECTOR,"input[type='search']")
search_box.send_keys("recherche")
search_box.submit()

# Collecter des informations sur les articles
articles = driver.find_elements(By.CSS_SELECTOR,".article")
for article in articles:
    titre = article.find_element(By.CSS_SELECTOR,".titre").text
    url = article.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
    print(titre, url)

# Fermer le navigateur
driver.quit()
