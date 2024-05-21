import time

from database.skills import SkillsDB
from database.users import UsersDB
from database.workers import WorkersDB
from pages.admin_page import AdminPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.worker_page import WorkersPage


def test_title(chrome_browser):
    driver = chrome_browser

    home = HomePage(driver)
    login = LoginPage(driver)
    admin = AdminPage(driver)
    worker = WorkersPage(driver)

    user_db = UsersDB()
    worker_db = WorkersDB()

    home.login_btn_click()
    login.fill_details_and_login("admin1@hireme.com", 'admin1')

    home.admin_dashboard()
    admin.view_all_admins()
    initial_users_count = user_db.count_of_users()
    admin.add_admin()
    admin.fill_details('Prathiksha', 'newadmin@hireme.com', 'newadmin')
    users_count_after_add = user_db.count_of_users()
    assert users_count_after_add == (initial_users_count + 1)

    user_id = user_db.find_user_id_by_email('newadmin@hireme.com')
    initial_value = user_db.get_value_from_db(user_id, 'name')
    admin.edit_admin_details('editedAdmin', 'admin2')
    after_edit_value = user_db.get_value_from_db(user_id, 'name')
    assert after_edit_value != initial_value

    home.admin_dashboard()
    admin.view_all_workers()

    worker_id = admin.reject()
    after_reject_status = worker_db.get_value_from_worker(worker_id, 'status')
    assert after_reject_status == 'rejected'

    home.pending_requests()
    worker_id_approve = admin.approve()
    after_approved_status = worker_db.get_value_from_worker(worker_id_approve, 'status')
    assert after_approved_status == 'approved'

    home.admin_dashboard()

    home.logout()
    time.sleep(5)
