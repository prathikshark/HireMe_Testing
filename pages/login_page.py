from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class LoginPage:
    SIGNUP_BTN_XPATH = "//a[contains(text(), 'Sign up')]"
    EMAIL_FIELD_XPATH = "//input[@id='user_email']"
    PASSWORD_FIELD_XPATH = "//input[@id='user_password']"
    LOGIN_BTN = "//input[@value='Log in']"

    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def sign_up_btn_click(self):
        signup_btn = self.obj.wait_till_present((By.XPATH, self.SIGNUP_BTN_XPATH))
        signup_btn.click()

    def fill_details_and_login(self, email, password):
        email_field = self.obj.wait_till_present((By.XPATH, self.EMAIL_FIELD_XPATH))
        self.obj.send_k(email_field, email)

        password_field = self.obj.wait_till_present((By.XPATH, self.PASSWORD_FIELD_XPATH))
        self.obj.send_k(password_field, password)

        login_btn = self.obj.wait_till_present((By.XPATH, self.LOGIN_BTN))
        login_btn.click()
