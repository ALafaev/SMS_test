from selenium import webdriver
import pytest

@pytest.fixture(scope="function") # Запускаем браузер и открываем сайт WB
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.wildberries.ru')
    yield driver
    driver.quit()