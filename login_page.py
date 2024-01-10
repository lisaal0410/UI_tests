from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('lisaal@gmail.com')

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys("never888")

    def go_to_button(self):
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        button.submit()
