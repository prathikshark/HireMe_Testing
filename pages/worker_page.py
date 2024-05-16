import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from base.base_code import BaseClass


class WorkersPage:
    COOKING_BTN = (By.XPATH, "//option[text()='cooking']")
    FROM_DATE_BTN = (By.XPATH, "//input[@id ='from_date']")
    TO_DATE_BTN = (By.XPATH, "//input[@id='worker_to_date']")
    SHIFT_BTN = (By.XPATH, " //select[@id = 'day_night_select']")
    GENDER_BTN = (By.XPATH, "//select[@id='gender_select']")
    SELECT_GENDER = (By.XPATH, "//option[@value='Male']")
    HOURS_PER_DAY = (By.XPATH, "//input[@id='hours_per_day_input']")
    TIMING = (By.XPATH, "//div[@id='timing_scroll']")
    SELECT_SLOT = (By.XPATH, "//*[@id='timing_scroll']/select/option[1]")
    APPLY_FILTER_BTN = (By.XPATH, "//input[@id='apply-filter-btn']")
    ADD_SERVICE_BTN = (By.XPATH, "//div[@class='c'][1]//button[text()='Add service']")

    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def apply_filter(self):
        time.sleep(3)
        cooking_btn = self.obj.wait_till_present(self.COOKING_BTN)
        cooking_btn.click()

        from_date_btn = self.obj.wait_till_present(self.FROM_DATE_BTN)
        self.obj.send_k(from_date_btn, '20-05-2024')

        to_date_btn = self.obj.wait_till_present(self.TO_DATE_BTN)
        self.obj.send_k(to_date_btn, '20-05-2024')

        shift_btn = self.obj.wait_till_present(self.SHIFT_BTN)
        self.obj.send_k(shift_btn, 'Day')

        gender_btn = self.obj.wait_till_present(self.GENDER_BTN)
        gender_btn.click()

        select_gender = self.obj.wait_till_present(self.SELECT_GENDER)
        select_gender.click()

        hours_per_day = self.obj.wait_till_present(self.HOURS_PER_DAY)
        self.obj.send_k(hours_per_day, 4)

        timing = self.obj.wait_till_present(self.TIMING)
        timing.click()

        select_slot = self.obj.wait_till_present(self.SELECT_SLOT)
        select_slot.click()

        apply_filter_btn = self.obj.wait_till_present(self.APPLY_FILTER_BTN)
        apply_filter_btn.click()
        time.sleep(3)

    def add_service(self):
        add_service_btn = self.obj.wait_till_clickable(self.ADD_SERVICE_BTN)
        add_service_btn.click()


