from typing import Tuple

from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.XPATH, "//div[@id='pv_id_2']/div/span")
    TYPE_DOG = (By.ID, "pv_id_2_0")
    TYPE_CAT = (By.ID, "pv_id_2_1")
    TYPE_REPTILE = (By.ID, "pv_id_2_2")
    TYPE_HAMSTER = (By.ID, "pv_id_2_3")
    TYPE_PARROT = (By.ID, "pv_id_2_4")
    FILTER_BY_NAME = (By.XPATH, "//*[@id='petName']")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    QUIT_BTN = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[2]/a[1]/span[1]')
    BTN_CREATE_PET = (By.CSS_SELECTOR, ".p-button-rounded")
    NAME_PET = (By.ID, "name")
    AGE_PET = (By.CSS_SELECTOR, 'input.p-inputtext:nth-child(1)')
    CHOOSE_PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    CHOOSE_PET_TYPE_DOG = (By.XPATH, '//*[@aria-label="dog"]')
    CHOOSE_PET_GENDER = (By.CSS_SELECTOR, '#genderSelector')
    CHOOSE_PET_GENDER_MALE = (By.XPATH, '//*[@aria-label="Male"]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '.pi-check')
    PET_DELETE_BTN = (By.CSS_SELECTOR, ".col-12:nth-child(4) .p-button-danger > .p-button-label")
    DELETE_CHOICE = (By.XPATH, "//span[contains(.,'Yes')]")
    EDIT_BTN = (By.CSS_SELECTOR, ".col-12:nth-child(2) .p-button:nth-child(1) > .p-button-label")
