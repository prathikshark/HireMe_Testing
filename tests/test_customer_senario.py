import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.worker_page import WorkersPage
from pages.booking_page import BookingsPage
from pages.customer_profile_page import CustomerProfilePage

from selenium.webdriver.common.by import By


def test_title(chrome_browser):

    driver = chrome_browser

    home = HomePage(driver)
    login = LoginPage(driver)
    register = RegistrationPage(driver)
    worker = WorkersPage(driver)
    booking = BookingsPage(driver)
    customer_profile = CustomerProfilePage(driver)

    home.login_btn_click()
    login.sign_up_btn_click()
    register.register_as_customer()

    home.service_btn_click()
    worker.apply_filter()
    worker.add_service()
    home.my_services()
    booking.remove_service()

    home.service_btn_click()
    worker.apply_filter()
    worker.add_service()
    home.my_services()

    booking.book()
    booking.confirm()
    home.profile()
    customer_profile.comment_and_rating()

    home.logout()
    time.sleep(10)
