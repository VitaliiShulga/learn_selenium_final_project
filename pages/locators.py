from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, '//div [@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div [@class="col-sm-6 product_main"]/p[1]')

    ADDED_PRODUCT_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    ADDED_PRODUCT_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//div [@class="alertinner "]')

