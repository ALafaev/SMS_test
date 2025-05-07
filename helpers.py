from locators import Locators

def show_first_ten_cards(driver):
    for i in range(0,9):
        product_name = driver.find_element(*Locators.get_name_locator_by_card_index(i)).get_attribute('aria-label')
        price = driver.find_element(*Locators.get_price_locator_by_card_index(i)).text
        print(f'{product_name} - {price}')
    return True
