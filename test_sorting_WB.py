from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


def show_first_ten_cards(driver): # Функция выводит на печать информацию о первых десяти карточках. В случае успешного вывода возвращает True.
    for i in range(0,9):
        product_name = driver.find_element(By.XPATH, f'.//article[@data-card-index="{i}"]//a').get_attribute('aria-label') # Используем динамический локатор для поиска названия товара
        price = driver.find_element(By.XPATH, f'.//article[@data-card-index="{i}"]//div[contains(@class, "card__price")]//ins').text # Используем динамический локатор для поиска цены товара
        print(f'{product_name} - {price}') # Выводим на печать полученную информацию в формате "Название - цена"
    return True

def test_sorting_by_prise_increase():
    driver = webdriver.Chrome() # Запускаем браузер Chrome
    driver.maximize_window() # Переводим окно браузера в полноэкранный режим
    driver.get('https://www.wildberries.ru') # Открываем главную страницу WB

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/input[@id="searchInput"]'))) # Ждем видимости строки поиска (поиск по XPath)
    driver.find_element(By.XPATH, './/input[@id="searchInput"]').send_keys('транспортир') # Вводим в строку поиска слово "транспортир"
    driver.find_element(By.XPATH, './/input[@id="searchInput"]').send_keys(Keys.ENTER) # Находясь в строке поиска, кликаем Enter
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/button[contains(@class,"dropdown-filter__btn--sorter")]'))) # Ждем видимости фильтра по цене
    driver.find_element(By.XPATH, './/button[contains(@class,"dropdown-filter__btn--sorter")]').click() # Кликаем на фильтр по цене
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/*[text()="По возрастанию цены"]'))) # Ждем появления фильтра "По возрастанию цены"
    driver.find_element(By.XPATH, './/*[text()="По возрастанию цены"]').click() # Кликаем на фильтр "По возрастанию цены"
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, './/button[contains(@class,"dropdown-filter__btn--sorter")]//div[text()="По возрастанию цены"]'))) # Ждем появления фильтра по цене в DOM дереве страницы
    sleep(1) # Пауза в 1 секунду (не лучшее решение, но в данном случае не нашел, за что еще можно зацепиться явным ожиданием)

    assert show_first_ten_cards(driver), "Список не сформирован" # Выводим карточки на печать, в случае успеха тест пройден.

    driver.quit() # Закрываем браузер
