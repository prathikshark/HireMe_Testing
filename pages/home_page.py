from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def login_btn_click(self):
        login_btn = self.obj.wait_till_visible((By.XPATH, "//a[contains(text(), 'Login')]"))
        login_btn.click()

    def service_btn_click(self):
        service_btn = self.obj.wait_till_visible((By.XPATH, "//a[text()='Service']"))
        service_btn.click()