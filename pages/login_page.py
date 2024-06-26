from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.SIGNUP_BTN_XPATH = "//a[contains(text(), 'Sign up')]"
        self.EMAIL_FIELD_XPATH = "//input[@id='user_email']"
        self.PASSWORD_FIELD_XPATH = "//input[@id='user_password']"
        self.LOGIN_BTN = "//input[@value='Log in']"

    def sign_up_btn_click(self):
        signup_btn = self.wait_till_present((By.XPATH, self.SIGNUP_BTN_XPATH))
        signup_btn.click()

    def fill_details_and_login(self, email, password):
        email_field = self.wait_till_present((By.XPATH, self.EMAIL_FIELD_XPATH))
        self.send_k(email_field, email)

        password_field = self.wait_till_present((By.XPATH, self.PASSWORD_FIELD_XPATH))
        self.send_k(password_field, password)

        login_btn = self.wait_till_present((By.XPATH, self.LOGIN_BTN))
        login_btn.click()
