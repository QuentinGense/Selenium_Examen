from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module")
def setup():
    # Initialiser le navigateur
    driver = webdriver.Chrome()
    yield driver
    # Fermer le navigateur après chaque test
    driver.quit()

def search_on_example_site(driver, keyword):
    # Ouvrir le site d'actualités/de commerce
    driver.get("https://example.com")

    # Effectuer une recherche si nécessaire
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )
    search_box.send_keys(keyword)
    search_box.submit()

def collect_article_information(driver):
    # Collecter des informations sur les articles
    articles = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".article"))
    )
    article_info = []
    for article in articles:
        title = article.find_element(By.CSS_SELECTOR, ".titre").text
        url = article.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        article_info.append((title, url))
    return article_info

def test_search_on_example_site(setup):
    driver = setup
    keyword = "recherche"

    search_on_example_site(driver, keyword)

    # Vérifier que la recherche a été effectuée avec succès
    assert keyword in driver.current_url

def test_collect_article_information(setup):
    driver = setup

    # Effectuer une recherche préalablement
    keyword = "recherche"
    search_on_example_site(driver, keyword)

    # Collecter des informations sur les articles
    article_info = collect_article_information(driver)

    # Vérifier que des informations d'article ont été collectées
    assert len(article_info) > 0
    for title, url in article_info:
        assert title.strip() != ""  # Vérifier que le titre n'est pas vide
        assert url.startswith("http")  # Vérifier que l'URL commence par "http"
