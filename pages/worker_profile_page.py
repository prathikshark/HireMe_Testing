import time
from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class WorkerProfilePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.ADD_SKILL_BTN_XPATH = (By.XPATH, "//button[text()='Add']")
        self.SELECT_SKILL_XPATH = "(//select[@id='worker_skill_id'])[1]"
        self.SELECT_SKILL_OPTION_XPATH = "(//option[text()='cooking'])[1]"
        self.EXPERIENCE_FIELD_XPATH = '(//input[@id="worker-skill-experience"])[1]'
        self.WAGE_FIELD_XPATH = '(//input[@id="worker-skill-wage"])[1]'
        self.ADD_SKILL_BTN_XPATH2 = '(//input[@id="add-worker-skill-btn"])[1]'
        self.REMOVE_SKILL_BTN_XPATH = '(//button[text()="Remove"])[1]'
        self.UPDATE_BTN_XPATH = '//button[text()="Update date"]'
        self.AGE_FIELD_XPATH = '//input[@id="worker_age"]'
        self.FROM_DATE_FIELD_XPATH = '//input[@id="worker_from_date"]'
        self.TO_DATE_FIELD_XPATH = '//input[@id="worker_to_date"]'
        self.SUBMIT_BTN_XPATH = '//input[@type="submit"]'

    def add_skill(self, experience, wage):
        add_skill_btn = self.wait_till_clickable(self.ADD_SKILL_BTN_XPATH)
        add_skill_btn.click()

        select_skill_btn = self.wait_till_present((By.XPATH, self.SELECT_SKILL_XPATH))
        time.sleep(1)
        select_skill_btn.click()

        select_skill = self.wait_till_present((By.XPATH, self.SELECT_SKILL_OPTION_XPATH))
        select_skill_btn = self. wait_till_present((By.XPATH, self.SELECT_SKILL_OPTION_XPATH))
        select_skill_btn.click()

        experience_field = self.wait_till_present((By.XPATH, self.EXPERIENCE_FIELD_XPATH))
        experience_field.clear()
        self.send_k(experience_field, experience)

        wage_field = self.wait_till_present((By.XPATH, self.WAGE_FIELD_XPATH))
        wage_field.clear()
        self.send_k(wage_field, wage)

        add_btn = self.wait_till_present((By.XPATH, self.ADD_SKILL_BTN_XPATH2))
        add_btn.click()

    def remove_skill(self):
        remove_worker_skill_btn = self.wait_till_present((By.XPATH, self.REMOVE_SKILL_BTN_XPATH))
        remove_worker_skill_btn.click()
        time.sleep(2)

    def update_data(self, from_date, to_date):
        update_btn = self.wait_till_present((By.XPATH, self.UPDATE_BTN_XPATH))
        update_btn.click()

        from_date_field = self.wait_till_present((By.XPATH, self.FROM_DATE_FIELD_XPATH))
        from_date_field.clear()
        self.send_k(from_date_field, from_date)

        to_date_field = self.wait_till_present((By.XPATH, self.TO_DATE_FIELD_XPATH))
        to_date_field.clear()
        self.send_k(to_date_field, to_date)

        submit_btn = self.wait_till_clickable((By.XPATH, self.SUBMIT_BTN_XPATH))
        submit_btn.click()
