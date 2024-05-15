import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class AdminPage:
    NAME_FIELD_XPATH = "//input[@id='user_name']"
    EMAIL_FIELD_XPATH = "//input[@id='user_email']"
    PASSWORD_FIELD_XPATH = "//input[@id='user_password']"
    VIEW_ALL_ADMINS_XPATH = "//a[text()='View All Admins']"
    ADD_ADMIN_BTN_XPATH = "//button[text()='Add Admin']"
    ADD_BTN_XPATH = "//input[@value='Add']"
    EDIT_BTN_XPATH = "(//button[text()='Edit'])[2]"
    UPDATE_BTN_XPATH = "//input[@value='Update']"
    APPROVE_BTN_XPATH = "//button[text()='Approve']"
    VIEW_ALL_WORKERS_XPATH = "//a[text()='View All Workers']"
    VIEW_ALL_SKILLS_XPATH = "//a[text()='View All Skills']"
    REJECT_BTN_XPATH = "(//button[text()='Reject'])[1]"
    REMOVE_SKILL_BTN_XPATH = "(//button[text()=' Remove'])[1]"
    CLOSE_MODAL_BTN = "//button[@class='btn-close']"

    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def view_all_admins(self):
        view_all_admins_btn = self.obj.wait_till_clickable((By.XPATH, self.VIEW_ALL_ADMINS_XPATH))
        view_all_admins_btn.click()

    def add_admin(self):
        add_admin_btn = self.obj.wait_till_clickable((By.XPATH, self.ADD_ADMIN_BTN_XPATH))
        add_admin_btn.click()

        close_modal_btn = self.obj.wait_till_clickable((By.XPATH, self.CLOSE_MODAL_BTN))
        close_modal_btn.click()

    def fill_details(self):
        name_field = self.obj.wait_till_present((By.XPATH, self.NAME_FIELD_XPATH))
        self.obj.send_k(name_field, 'Prathiksha')

        email_field = self.obj.wait_till_present((By.XPATH, self.EMAIL_FIELD_XPATH))
        self.obj.send_k(email_field, 'admin3@hireme.com')

        password_field = self.obj.wait_till_present((By.XPATH, self.PASSWORD_FIELD_XPATH))
        self.obj.send_k(password_field, 'admin3')

        add_btn = self.obj.wait_till_clickable((By.XPATH, self.ADD_BTN_XPATH))
        add_btn.click()
        time.sleep(2)

    def edit_admin_details(self):
        edit_btn = self.obj.wait_till_clickable((By.XPATH, self.EDIT_BTN_XPATH))
        try:
            edit_btn.click()
        except ElementClickInterceptedException:
            time.sleep(3)
            edit_btn.click()

        name_field = self.obj.wait_till_present((By.XPATH, self.NAME_FIELD_XPATH))
        name_field.clear()
        self.obj.send_k(name_field, 'new admin')

        email_field = self.obj.wait_till_present((By.XPATH, self.EMAIL_FIELD_XPATH))
        email_field.clear()
        self.obj.send_k(email_field, 'newadmin@hireme.com')

        password_field = self.obj.wait_till_present((By.XPATH, self.PASSWORD_FIELD_XPATH))
        password_field.clear()
        self.obj.send_k(password_field, 'newadmin')

        update_btn = self.obj.wait_till_clickable((By.XPATH, self.UPDATE_BTN_XPATH))
        update_btn.click()

    def approve(self):
        approve_btn = self.obj.wait_till_clickable((By.XPATH, self.APPROVE_BTN_XPATH))
        approve_btn.click()

    def view_all_workers(self):
        view_all_workers_btn = self.obj.wait_till_clickable((By.XPATH, self.VIEW_ALL_WORKERS_XPATH))
        view_all_workers_btn.click()

    def view_all_skills(self):
        view_all_skills_btn = self.obj.wait_till_clickable((By.XPATH, self.VIEW_ALL_SKILLS_XPATH))
        view_all_skills_btn.click()

    def reject(self):
        reject_btn = self.obj.wait_till_clickable((By.XPATH, self.REJECT_BTN_XPATH))
        reject_btn.click()

    def remove_skill(self):
        remove_skill_btn = self.obj.wait_till_clickable((By.XPATH, self.REMOVE_SKILL_BTN_XPATH))
        remove_skill_btn.click()
