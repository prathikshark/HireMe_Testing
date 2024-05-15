import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from base.base_code import BaseClass


class WorkerProfilePage:
    ADD_SKILL_BTN_XPATH = (By.XPATH, "//button[text()='Add']")

    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def add_skill(self):
        add_skill_btn = self.obj.wait_till_clickable(self.ADD_SKILL_BTN_XPATH)
        try:
            add_skill_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            add_skill_btn.click()

            # skill table id dup
        select_skill_btn = self.obj.wait_till_present((By.XPATH, "(//select[@id='worker_skill_id'])[1]"))
        time.sleep(1)
        select_skill_btn.click()

        select_skill = self.obj.wait_till_present((By.XPATH, "(//option[text()='cooking'])[1]"))
        select_skill.click()

        experience_field = self.obj.wait_till_present((By.XPATH, '(//input[@id="worker-skill-experience"])[1]'))
        experience_field.clear()
        self.obj.send_k(experience_field, '1 year')

        wage_field = self.obj.wait_till_present((By.XPATH, '(//input[@id="worker-skill-wage"])[1]'))
        wage_field.clear()
        self.obj.send_k(wage_field, 300)

        add_btn = self.obj.wait_till_present((By.XPATH, '(//input[@id="add-worker-skill-btn"])[1]'))
        add_btn.click()

    def remove_skill(self):
        remove_worker_skill_btn = self.obj.wait_till_present((By.XPATH, '(//button[text()="Remove"])[1]'))
        try:
            remove_worker_skill_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            remove_worker_skill_btn.click()

    def update_data(self):
        update_btn = self.obj.wait_till_present((By.XPATH, '//button[text()="Update date"]'))
        try:
            update_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            update_btn.click()

        age = self.obj.wait_till_present((By.XPATH, '//input[@id="worker_age"]'))
        self.obj.send_k(age, '24')

        from_date = self.obj.wait_till_present((By.XPATH, '//input[@id="worker_from_date"]'))
        self.obj.send_k(from_date, '24-05-2024')

        to_date = self.obj.wait_till_present((By.XPATH, '//input[@id="worker_to_date"]'))
        self.obj.send_k(to_date, '30-05-2024')

        submit_btn = self.obj.wait_till_clickable((By.XPATH, '//input[@type="submit"]'))
        try:
            submit_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            submit_btn.click()
