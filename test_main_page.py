from pages.main_page import MainPage
import time
from selenium.webdriver.common.keys import Keys


def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_filter_by_type_dog(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_type()
    page.find_type_dog()
    time.sleep(2)


def test_filter_by_type_cat(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_type()
    page.find_type_cat()
    time.sleep(2)


def test_filter_by_type_reptile(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_type()
    page.find_type_reptile()
    time.sleep(2)


def test_filter_by_type_hamster(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_type()
    page.find_type_hamster()
    time.sleep(2)


def test_filter_by_type_parrot(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_type()
    page.find_type_parrot()
    time.sleep(2)


# @pytest.mark.skip
def test_filter_by_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_name()
    time.sleep(4)
    page.go_to_name()
    time.sleep(4)
