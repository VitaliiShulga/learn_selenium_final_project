from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_promo_newYear_url(self):
        assert "?promo=newYear" in self.browser.current_url, '"newYear" not in url'

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button add to basket not on the screen"

    def product_in_basket(self):
        self.product_name_must_match()
        self.product_price_must_match()

    def product_name_must_match(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert name.text == added_name.text, 'No Much'


    def product_price_must_match(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        assert price.text in added_price.text, "Price no much"

