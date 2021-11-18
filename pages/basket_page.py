from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FORMS) == False, "Basket not empty"

    def should_be_text_obout_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET).text
        assert "basket is empty" in text, "Basket not empty"



