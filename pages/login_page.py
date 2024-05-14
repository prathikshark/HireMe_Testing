from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def sign_up_btn_click(self):
        signup_btn = self.obj.wait_till_visible((By.XPATH, "// a[contains(text(), 'Sign up')]"))
        signup_btn.click()


