import time

from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class WorkersPage:
    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def apply_filter(self):
        select_service_btn = self.obj.wait_till_visible((By.XPATH, '//*[@id="skill_type"]'))
        select_service_btn.click()

        cooking_btn = self.obj.wait_till_present((By.XPATH, "//option[text()='cooking']"))
        cooking_btn.click()

        from_date_btn = self.obj.wait_till_present((By.XPATH, "//input[@id ='from_date']"))
        self.obj.send_k(from_date_btn, '31-05-2024')

        to_date_btn = self.obj.wait_till_present((By.XPATH, "//input[@id='worker_to_date']"))
        self.obj.send_k(to_date_btn, '31-05-2024')

        shift_btn = self.obj.wait_till_present((By.XPATH, " //select[@id = 'day_night_select']"))
        self.obj.send_k(shift_btn, 'Day')

        gender_btn = self.obj.wait_till_present((By.XPATH, "//select[@id='gender_select']"))
        gender_btn.click()

        select_gender = self.obj.wait_till_present((By.XPATH, "//option[@value='Male']"))
        select_gender.click()

        hours_per_day = self.obj.wait_till_present((By.XPATH, "//input[@id='hours_per_day_input']"))
        self.obj.send_k(hours_per_day, 4)

        timing = self.obj.wait_till_present((By.XPATH, "//div[@id='timing_scroll']"))
        timing.click()

        select_slot = self.obj.wait_till_present((By.XPATH, "//*[@id='timing_scroll']/select/option[1]"))
        select_slot.click()

        apply_filter_btn = self.obj.wait_till_present((By.XPATH, "//input[@id='apply-filter-btn']"))
        apply_filter_btn.click()
        time.sleep(3)

    def add_service(self):
        add_service_btn = self.obj.wait_till_present((By.XPATH, "//div[@class='c'][1]//button[text()='Add service']"))
        add_service_btn.click()

    # select_service_btn = self.obj.wait_till_visible((By.XPATH, "//*[@id='skill_type'])]"))
    # select_service_btn.click()
