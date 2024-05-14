import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.workers_page import WorkersPage

from selenium.webdriver.common.by import By


def test_title(chrome_browser):

    driver = chrome_browser

    home = HomePage(driver)
    login = LoginPage(driver)
    register = RegistrationPage(driver)
    worker = WorkersPage(driver)

    home.login_btn_click()
    login.sign_up_btn_click()
    register.register_as_customer()
    home.service_btn_click()
    worker.apply_filter()
    worker.add_service()

    time.sleep(10)
