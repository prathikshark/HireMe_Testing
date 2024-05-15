import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class AdminPage:
    NAME_FIELD_XPATH = "//input[@id='user_name']"
    EMAIL_FIELD_XPATH = "//input[@id='user_email']"
    PASSWORD_FIELD_XPATH = "//input[@id='user_password']"

    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def view_all_admins(self):
        view_all_admins_btn = self.obj.wait_till_clickable((By.XPATH, "//a[text()='View All Admins']"))
        view_all_admins_btn.click()

    def add_admin(self):
        add_admin_btn = self.obj.wait_till_clickable((By.XPATH, "//button[text()='Add Admin']"))
        add_admin_btn.click()

    def fill_details(self):
        name_field = self.obj.wait_till_present((By.XPATH, self.NAME_FIELD_XPATH))
        self.obj.send_k(name_field, 'Prathiksha')

        email_field = self.obj.wait_till_present((By.XPATH, self.EMAIL_FIELD_XPATH))
        self.obj.send_k(email_field, 'admin3@hireme.com')

        password_field = self.obj.wait_till_present((By.XPATH, self.PASSWORD_FIELD_XPATH))
        self.obj.send_k(password_field, 'admin3')

        add_btn = self.obj.wait_till_clickable((By.XPATH, "//input[@value='Add']"))
        add_btn.click()
        time.sleep(2)

    def edit_admin_details(self):
        edit_btn = self.obj.wait_till_clickable((By.XPATH, "(//button[text()='Edit'])[2]"))
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

        update_btn = self.obj.wait_till_clickable((By.XPATH, "//input[@value='Update']"))
        update_btn.click()

    def approve(self):
        approve_btn = self.obj.wait_till_clickable((By.XPATH, "//button[text()='Approve']"))
        approve_btn.click()

    def view_all_workers(self):
        view_all_workers_btn = self.obj.wait_till_clickable((By.XPATH, "//a[text()='View All Workers']"))
        view_all_workers_btn.click()

    def view_all_skills(self):
        view_all_skills_btn = self.obj.wait_till_clickable((By.XPATH, "//a[text()='View All Skills']"))
        view_all_skills_btn.click()

    def reject(self):
        reject_btn = self.obj.wait_till_clickable((By.XPATH, "(//button[text()='Reject'])[1]"))
        reject_btn.click()

    def remove_skill(self):
        remove_skill_btn = self.obj.wait_till_clickable((By.XPATH, "(//button[text()=' Remove'])[1]"))
        remove_skill_btn.click()
