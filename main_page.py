from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def filter_by_type(self):
        filter_link = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        filter_link.click()

    def find_type_dog(self):
        type_dog = self.browser.find_element(*MainPageLocators.TYPE_DOG)
        type_dog.click()

    def find_type_cat(self):
        type_cat = self.browser.find_element(*MainPageLocators.TYPE_CAT)
        type_cat.click()

    def find_type_reptile(self):
        type_reptile = self.browser.find_element(*MainPageLocators.TYPE_REPTILE)
        type_reptile.click()

    def find_type_hamster(self):
        type_hamster = self.browser.find_element(*MainPageLocators.TYPE_HAMSTER)
        type_hamster.click()

    def find_type_parrot(self):
        type_parrot = self.browser.find_element(*MainPageLocators.TYPE_PARROT)
        type_parrot.click()

    def filter_by_pet_name(self):
        filter_link = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        filter_link.click()

    def go_to_name(self):
        name = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        name.send_keys("Bob")
        name.send_keys(Keys.ENTER)
