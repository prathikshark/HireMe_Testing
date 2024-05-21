import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class AdminPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.NAME_FIELD_XPATH = "//input[@id='user_name']"
        self.EMAIL_FIELD_XPATH = "//input[@id='user_email']"
        self.VIEW_ALL_ADMINS_XPATH = "//a[text()='View All Admins']"
        self.PASSWORD_FIELD_XPATH = "//input[@id='user_password']"
        self.ADD_ADMIN_BTN_XPATH = "//button[text()='Add Admin']"
        self.ADD_BTN_XPATH = "//input[@value='Add']"
        self.EDIT_BTN_XPATH = "(//button[text()='Edit'])[3]"
        self.UPDATE_BTN_XPATH = "//input[@value='Update']"
        self.APPROVE_BTN_XPATH = "//button[text()='Approve']"
        self.VIEW_ALL_WORKERS_XPATH = "//a[text()='View All Workers']"
        self.VIEW_ALL_SKILLS_XPATH = "//a[text()='View All Skills']"
        self.REJECT_BTN_XPATH = "(//button[text()='Reject'])[1]"
        self.REMOVE_SKILL_BTN_XPATH = "(//button[text()=' Remove'])[1]"
        self.CLOSE_MODAL_BTN = "//button[@class='btn-close']"

    def view_all_admins(self):
        view_all_admins_btn = self.wait_till_clickable((By.XPATH, self.VIEW_ALL_ADMINS_XPATH))
        view_all_admins_btn.click()

    def add_admin(self):
        add_admin_btn = self.wait_till_clickable((By.XPATH, self.ADD_ADMIN_BTN_XPATH))
        add_admin_btn.click()

    def fill_details(self, name, email, password):
        name_field = self.wait_till_present((By.XPATH, self.NAME_FIELD_XPATH))
        self.send_k(name_field, name)

        email_field = self.wait_till_present((By.XPATH, self.EMAIL_FIELD_XPATH))
        self.send_k(email_field, email)

        password_field = self.wait_till_present((By.XPATH, self.PASSWORD_FIELD_XPATH))
        self.send_k(password_field, password)

        add_btn = self.wait_till_clickable((By.XPATH, self.ADD_BTN_XPATH))
        add_btn.click()

    def edit_admin_details(self, name, password):
        edit_btn = self.wait_till_clickable((By.XPATH, self.EDIT_BTN_XPATH))
        edit_btn.click()

        name_field = self.wait_till_present((By.XPATH, self.NAME_FIELD_XPATH))
        name_field.clear()
        self.send_k(name_field, name)

        password_field = self.wait_till_present((By.XPATH, self.PASSWORD_FIELD_XPATH))
        self.send_k(password_field, name)

        update_btn = self.wait_till_clickable((By.XPATH, self.UPDATE_BTN_XPATH))
        update_btn.click()

    def approve(self):
        approve_btn = self.wait_till_clickable((By.XPATH, self.APPROVE_BTN_XPATH))
        worker_id_approve = approve_btn.get_attribute('data-worker-id')
        approve_btn.click()
        time.sleep(2)
        return worker_id_approve

    def view_all_workers(self):
        view_all_workers_btn = self.wait_till_clickable((By.XPATH, self.VIEW_ALL_WORKERS_XPATH))
        view_all_workers_btn.click()

    def view_all_skills(self):
        view_all_skills_btn = self.wait_till_clickable((By.XPATH, self.VIEW_ALL_SKILLS_XPATH))
        view_all_skills_btn.click()

    def reject(self):
        reject_btn = self.wait_till_clickable((By.XPATH, self.REJECT_BTN_XPATH))
        worker_id = reject_btn.get_attribute('data-worker-id')
        reject_btn.click()
        time.sleep(2)
        return worker_id

    def remove_skill(self):
        remove_skill_btn = self.wait_till_clickable((By.XPATH, self.REMOVE_SKILL_BTN_XPATH))
        remove_skill_btn.click()
        time.sleep(10)
