import time

from database.skills import SkillsDB
from database.users import UsersDB
from database.workers import WorkersDB
from pages.admin_page import AdminPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_title(chrome_browser):
    driver = chrome_browser

    home = HomePage(driver)
    login = LoginPage(driver)
    admin = AdminPage(driver)

    user_db = UsersDB()
    worker_db = WorkersDB()
    skill_db = SkillsDB()

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
    # time.sleep(2)
    after_edit_value = user_db.get_value_from_db(user_id, 'name')
    assert after_edit_value != initial_value

    home.admin_dashboard()
    admin.view_all_workers()

    initial_status = worker_db.get_value_from_worker(user_id, 'status')
    after_reject_status = worker_db.get_value_from_worker(user_id, 'status')
    assert initial_status != after_reject_status

    home.pending_requests()
    admin.approve()
    after_approved_status = worker_db.get_value_from_worker(user_id, 'status')
    assert after_approved_status == 'approved'

    home.admin_dashboard()
    admin.view_all_skills()

    initial_count_of_skills = skill_db.get_count_of_skills()
    admin.remove_skill()
    assert skill_db.get_count_of_skills() == initial_count_of_skills - 1

    home.logout()
    time.sleep(10)
