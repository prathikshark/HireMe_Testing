import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from base.base_code import BaseClass


class CustomerProfilePage:
    COMMENT_FIELD = (By.XPATH, "(//input[@class='comment'])[1]")
    RATING_FIELD = (By.XPATH, "(//input[@class='rating'])[1]")
    SUBMIT_FEEDBACK_BTN = (By.XPATH, "(//input[@type='submit'])[1]")

    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def comment_and_rating(self):
        comment_field = self.obj.wait_till_present(self.COMMENT_FIELD)
        comment_field.send_keys("Great service")

        rating_field = self.obj.wait_till_present(self.RATING_FIELD)
        rating_field.send_keys(4)

        submit_feedback_btn = self.obj.wait_till_present(self.SUBMIT_FEEDBACK_BTN)
        try:
            submit_feedback_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            submit_feedback_btn.click()
