from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class CustomerProfilePage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.COMMENT_FIELD = (By.XPATH, "(//input[@class='comment'])[1]")
        self.RATING_FIELD = (By.XPATH, "(//input[@class='rating'])[1]")
        self.SUBMIT_FEEDBACK_BTN = (By.XPATH, "(//input[@type='submit'])[1]")

    def comment_and_rating(self):
        comment_field = self.wait_till_present(self.COMMENT_FIELD)
        comment_field.send_keys("Great service")

        rating_field = self.wait_till_present(self.RATING_FIELD)
        rating_field.send_keys(4)

        submit_feedback_btn = self.wait_till_present(self.SUBMIT_FEEDBACK_BTN)
        serviceId = submit_feedback_btn.get_attribute('data-serviceid')
        submit_feedback_btn.click()

        return serviceId
