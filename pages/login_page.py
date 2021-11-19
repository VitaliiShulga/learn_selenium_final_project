from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, '"login" not in url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not on the page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form not on the page"

    def register_new_user(self,):
        password = '1234qwertyuiop'
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*LoginPageLocators.LOGIN_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
