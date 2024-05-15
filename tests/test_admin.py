import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.worker_page import WorkersPage
from pages.booking_page import BookingsPage
from pages.worker_profile_page import WorkerProfilePage
from pages.admin_page import AdminPage


def test_title(chrome_browser):
    driver = chrome_browser

    home = HomePage(driver)
    login = LoginPage(driver)
    register = RegistrationPage(driver)
    worker = WorkersPage(driver)
    booking = BookingsPage(driver)
    worker_profile = WorkerProfilePage(driver)
    admin = AdminPage(driver)

    home.login_btn_click()
    login.fill_details_and_login()
    home.close_flash()

    home.admin_dashboard()
    admin.view_all_admins()
    admin.add_admin()
    admin.fill_details()
    admin.edit_admin_details()

    home.admin_dashboard()
    admin.view_all_workers()
    admin.reject()
    home.pending_requests()
    # admin.approve()

    home.admin_dashboard()
    admin.view_all_skills()
    admin.remove_skill()

    home.logout()
    time.sleep(10)
