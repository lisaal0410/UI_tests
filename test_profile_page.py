from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import time


# @pytest.mark.smoke
def test_quit_profile(browser):
    link = "http://34.141.58.52:8080/#/profile"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    time.sleep(3)
    page = ProfilePage(browser, link)
    page.quit_profile()
    time.sleep(3)


def test_go_to_create_pet(browser):
    link = "http://34.141.58.52:8080/#/profile"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    time.sleep(3)
    page = ProfilePage(browser, link)
    page.go_to_create()
    time.sleep(2)
    page.pet_name()
    page.pet_age()
    page.pet_type()
    page.select_dog()
    time.sleep(3)
    page.pet_gender()
    page.pet_gender_dog()
    time.sleep(3)
    page.go_to_button()
    time.sleep(3)


def test_delete_pet(browser):
    link = "http://34.141.58.52:8080/#/profile"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    page = ProfilePage(browser, link)
    page.delete_pet()
    page.delete_choice()
    time.sleep(3)


def test_edit_pet_card(browser):
    link = "http://34.141.58.52:8080/#/profile"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    page = ProfilePage(browser, link)
    page.edit_pet_card()
    time.sleep(4)
    page.change_name()
    time.sleep(4)
    page.go_to_submit()
    time.sleep(3)
