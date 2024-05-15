import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from base.base_code import BaseClass

class WorkerProfilePage:
    ADD_SKILL_BTN_XPATH = (By.XPATH, "//button[text()='Add']")
    SELECT_SKILL_XPATH = "(//select[@id='worker_skill_id'])[1]"
    SELECT_SKILL_OPTION_XPATH = "(//option[text()='cooking'])[1]"
    EXPERIENCE_FIELD_XPATH = '(//input[@id="worker-skill-experience"])[1]'
    WAGE_FIELD_XPATH = '(//input[@id="worker-skill-wage"])[1]'
    ADD_SKILL_BTN_XPATH2 = '(//input[@id="add-worker-skill-btn"])[1]'
    REMOVE_SKILL_BTN_XPATH = '(//button[text()="Remove"])[1]'
    UPDATE_BTN_XPATH = '//button[text()="Update date"]'
    AGE_FIELD_XPATH = '//input[@id="worker_age"]'
    FROM_DATE_FIELD_XPATH = '//input[@id="worker_from_date"]'
    TO_DATE_FIELD_XPATH = '//input[@id="worker_to_date"]'
    SUBMIT_BTN_XPATH = '//input[@type="submit"]'

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

        select_skill_btn = self.obj.wait_till_present((By.XPATH, self.SELECT_SKILL_XPATH))
        time.sleep(1)
        select_skill_btn.click()

        select_skill = self.obj.wait_till_present((By.XPATH, self.SELECT_SKILL_OPTION_XPATH))
        select_skill.click()

        experience_field = self.obj.wait_till_present((By.XPATH, self.EXPERIENCE_FIELD_XPATH))
        experience_field.clear()
        self.obj.send_k(experience_field, '1 year')

        wage_field = self.obj.wait_till_present((By.XPATH, self.WAGE_FIELD_XPATH))
        wage_field.clear()
        self.obj.send_k(wage_field, 300)

        add_btn = self.obj.wait_till_present((By.XPATH, self.ADD_SKILL_BTN_XPATH2))
        add_btn.click()

    def remove_skill(self):
        remove_worker_skill_btn = self.obj.wait_till_present((By.XPATH, self.REMOVE_SKILL_BTN_XPATH))
        try:
            remove_worker_skill_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            remove_worker_skill_btn.click()

    def update_data(self):
        update_btn = self.obj.wait_till_present((By.XPATH, self.UPDATE_BTN_XPATH))
        try:
            update_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            update_btn.click()

        age = self.obj.wait_till_present((By.XPATH, self.AGE_FIELD_XPATH))
        self.obj.send_k(age, '24')

        from_date = self.obj.wait_till_present((By.XPATH, self.FROM_DATE_FIELD_XPATH))
        self.obj.send_k(from_date, '24-05-2024')

        to_date = self.obj.wait_till_present((By.XPATH, self.TO_DATE_FIELD_XPATH))
        self.obj.send_k(to_date, '30-05-2024')

        submit_btn = self.obj.wait_till_clickable((By.XPATH, self.SUBMIT_BTN_XPATH))
        try:
            submit_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            submit_btn.click()
