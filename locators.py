from selenium.webdriver.common.by import By

class Locators:
    SEARCH_INPUT = [By.XPATH, './/input[@id="searchInput"]']
    CHOOSE_FILTER_FIELD = [By.XPATH, './/button[contains(@class,"dropdown-filter__btn--sorter")]']
    FILTER_BY_PRICE_INCREASE = [By.XPATH, './/button[contains(@class,"dropdown-filter__btn--sorter")]//div[text()="По возрастанию цены"]']
    PRISE_INCREASE_FILTER = [By.XPATH, './/*[text()="По возрастанию цены"]']

    @staticmethod
    def get_name_locator_by_card_index(i):
        return [By.XPATH, f'.//article[@data-card-index="{i}"]//a']

    @staticmethod
    def get_price_locator_by_card_index(i):
        return [By.XPATH, f'.//article[@data-card-index="{i}"]//div[contains(@class, "card__price")]//ins']
