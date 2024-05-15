import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.worker_page import WorkersPage
from pages.booking_page import BookingsPage
from pages.customer_profile_page import CustomerProfilePage
from database.users import UsersDB
from database.bookings import BookingsDB
from database.booked_services import BookedServicesDB

from selenium.webdriver.common.by import By


def test_title(chrome_browser):
    driver = chrome_browser

    home = HomePage(driver)
    login = LoginPage(driver)
    register = RegistrationPage(driver)
    worker = WorkersPage(driver)
    booking = BookingsPage(driver)
    customer_profile = CustomerProfilePage(driver)
    udb = UsersDB()
    booking_db = BookingsDB()
    booked_service_db = BookedServicesDB()

    home.login_btn_click()
    login.sign_up_btn_click()
    initial_users_count = udb.count_of_users()
    time.sleep(2)
    register.register_as_customer('Aman', 'marathalli', '1111111111', 'amannn1@gmail.com', '111111', '111111')
    users_count_after_add = udb.count_of_users()
    assert users_count_after_add == (initial_users_count + 1)

    home.service_btn_click()
    worker.apply_filter()
    initial_booked_service_count = booked_service_db.count_of_booked_services()
    worker.add_service()
    after_add_booked_service_count = booked_service_db.count_of_booked_services()
    assert after_add_booked_service_count == (initial_booked_service_count + 1)

    home.my_services()
    booking.remove_service()
    time.sleep(2)
    after_delete_booked_service_count = booked_service_db.count_of_booked_services()
    assert after_delete_booked_service_count == (after_add_booked_service_count - 1)

    home.service_btn_click()
    worker.apply_filter()
    worker.add_service()
    home.my_services()

    booking.confirm()
    time.sleep(5)

    home.profile()
    customer_profile.comment_and_rating()
    home.close_flash()
    home.logout()

    time.sleep(10)
