import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.worker_page import WorkersPage
from pages.booking_page import BookingsPage
from pages.worker_profile_page import WorkerProfilePage


def test_title(chrome_browser):
    driver = chrome_browser

    home = HomePage(driver)
    login = LoginPage(driver)
    register = RegistrationPage(driver)
    worker = WorkersPage(driver)
    booking = BookingsPage(driver)
    worker_profile = WorkerProfilePage(driver)

    home.login_btn_click()
    login.fill_details_and_login()
    home.close_flash()
    home.profile()
    worker_profile.add_skill()
    worker_profile.remove_skill()
    worker_profile.add_skill()
    worker_profile.update_data()
    home.logout()

    time.sleep(10)
