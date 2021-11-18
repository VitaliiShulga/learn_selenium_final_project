from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def success_message_should_desapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"