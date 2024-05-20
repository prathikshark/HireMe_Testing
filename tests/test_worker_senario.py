import time
from database.users import UsersDB
from database.workers import WorkersDB
from database.worker_skills import WorkerSkillsDB
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
    worker_profile = WorkerProfilePage(driver)
    worker_db = WorkersDB()
    workerSkillDB = WorkerSkillsDB()
    user_db = UsersDB()

    home.login_btn_click()
    login.fill_details_and_login("purav@gmail.com", "111111")
    home.close_flash()
    home.profile()

    user_id = user_db.find_user_id_by_email('purav@gmail.com')
    worker_id = worker_db.find_worker_id_by_user_id(user_id)

    initial_worker_skill_count = workerSkillDB.count_of_worker_skills(worker_id)
    worker_profile.add_skill('1 year', 200)
    after_add_worker_skill_count = workerSkillDB.count_of_worker_skills(worker_id)
    assert initial_worker_skill_count == after_add_worker_skill_count

    worker_profile.remove_skill()
    after_delete_worker_skill_count = workerSkillDB.count_of_worker_skills(worker_id)
    assert after_delete_worker_skill_count == after_add_worker_skill_count - 1

    worker_profile.add_skill('2 years', 500)
    worker_profile.update_data('26-05-2024', '05-06-2024')
    from_date = worker_db.get_from_and_to_date(worker_id, 'from_date')
    to_date = worker_db.get_from_and_to_date(worker_id, 'to_date')
    assert from_date == '26-05-2024' and to_date == '05-06-2024'

    home.close_flash()
    home.logout()

    time.sleep(10)
