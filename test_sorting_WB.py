from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import Locators
from helpers import show_first_ten_cards
from time import sleep


class TestSortingWB:

    def test_sorting_by_prise_increase(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SEARCH_INPUT))
        driver.find_element(*Locators.SEARCH_INPUT).send_keys('транспортир')
        driver.find_element(*Locators.SEARCH_INPUT).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHOOSE_FILTER_FIELD))
        driver.find_element(*Locators.CHOOSE_FILTER_FIELD).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PRISE_INCREASE_FILTER))
        driver.find_element(*Locators.PRISE_INCREASE_FILTER).click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located(Locators.FILTER_BY_PRICE_INCREASE))
        sleep(1)

        assert show_first_ten_cards(driver), "Список не сформирован"
