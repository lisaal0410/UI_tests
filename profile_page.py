from selenium.webdriver.common.by import By
from .locators import ProfilePageLocators
from .base_page import BasePage


class ProfilePage(BasePage):

    def go_to_create(self):
        button = self.browser.find_element(*ProfilePageLocators.BTN_CREATE_PET)
        button.click()

    def pet_name(self):
        name = self.browser.find_element(*ProfilePageLocators.NAME_PET)
        name.send_keys('Doge')

    def pet_age(self):
        age = self.browser.find_element(*ProfilePageLocators.AGE_PET)
        age.send_keys('2')

    def pet_type(self):
        type = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_TYPE)
        type.click()

    def select_dog(self):
        type_pet = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_TYPE_DOG)
        type_pet.click()

    def pet_gender(self):
        gender = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_GENDER)
        gender.click()

    def pet_gender_dog(self):
        gender_dog = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_GENDER_MALE)
        gender_dog.click()

    def go_to_button(self):
        button = self.browser.find_element(*ProfilePageLocators.BUTTON_SUBMIT)
        button.click()

    def delete_pet(self):
        delete = self.browser.find_element(*ProfilePageLocators.PET_DELETE_BTN)
        delete.click()

    def delete_choice(self):
        choice = self.browser.find_element(*ProfilePageLocators.DELETE_CHOICE)
        choice.click()

    def edit_pet_card(self):
        edit = self.browser.find_element(*ProfilePageLocators.EDIT_BTN)
        edit.click()

    def change_name(self):
        change_name = self.browser.find_element(*ProfilePageLocators.NAME_PET)
        change_name.clear()
        change_name = change_name.send_keys("Maya")

    def go_to_submit(self):
        button_submit = self.browser.find_element(*ProfilePageLocators.BUTTON_SUBMIT)
        button_submit.click()

    def quit_profile(self):
        quit = self.browser.find_element(*ProfilePageLocators.QUIT_BTN)
        quit.click()
