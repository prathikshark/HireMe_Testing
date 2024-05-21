import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_code import BaseClass


class WorkersPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.COOKING_BTN = (By.XPATH, "//option[text()='cooking']")
        self.FROM_DATE_BTN = (By.XPATH, "//input[@id ='from_date']")
        self.TO_DATE_BTN = (By.XPATH, "//input[@id='worker_to_date']")
        self.SHIFT_BTN = (By.XPATH, " //select[@id = 'day_night_select']")
        self.GENDER_BTN = (By.XPATH, "//select[@id='gender_select']")
        self.SELECT_GENDER = (By.XPATH, "//option[@value='Male']")
        self.HOURS_PER_DAY = (By.XPATH, "//input[@id='hours_per_day_input']")
        self.TIMING = (By.XPATH, "//div[@id='timing_scroll']")
        self.SELECT_SLOT = (By.XPATH, "//*[@id='timing_scroll']/select/option[1]")
        self.APPLY_FILTER_BTN = (By.XPATH, "//input[@id='apply-filter-btn']")
        self.ADD_SERVICE_BTN = (By.XPATH, "//div[@class='c'][1]//button[text()='Add service']")

    def apply_filter(self):
        time.sleep(3)
        cooking_btn = self.wait_till_present(self.COOKING_BTN)
        cooking_btn.click()

        from_date_btn = self.wait_till_present(self.FROM_DATE_BTN)
        self.send_k(from_date_btn, '23-05-2024')

        to_date_btn = self.wait_till_present(self.TO_DATE_BTN)
        self.send_k(to_date_btn, '23-05-2024')

        shift_btn = self.wait_till_present(self.SHIFT_BTN)
        self.send_k(shift_btn, 'Day')

        gender_btn = self.wait_till_present(self.GENDER_BTN)
        gender_btn.click()

        select_gender = self.wait_till_present(self.SELECT_GENDER)
        select_gender.click()

        hours_per_day = self.wait_till_present(self.HOURS_PER_DAY)
        self.send_k(hours_per_day, 4)

        timing = self.wait_till_present(self.TIMING)
        timing.click()

        select_slot = self.wait_till_present(self.SELECT_SLOT)
        select_slot.click()

        apply_filter_btn = self.wait_till_present(self.APPLY_FILTER_BTN)
        apply_filter_btn.click()

    def add_service(self):
        add_service_btn = self.wait_till_clickable(self.ADD_SERVICE_BTN)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(add_service_btn)
        add_service_btn.click()
        time.sleep(2)
