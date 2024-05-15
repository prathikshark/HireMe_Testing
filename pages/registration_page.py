from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class RegistrationPage:
    NAME_FIELD_XPATH = "//input[@id='user_name']"
    ADDRESS_FIELD_XPATH = "//input[@id='user_address']"
    PHONE_FIELD_XPATH = "//input[@id='user_phone']"
    EMAIL_FIELD_XPATH = "//input[@id='user_email']"
    PASSWORD_FIELD_XPATH = "//input[@id='user_password']"
    PASSWORD_CONFIRMATION_FIELD_XPATH = "//input[@id='user_password_confirmation']"
    SIGNUP_BTN_XPATH = "//input[@id='submit-btn']"

    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def register_as_customer(self, name, address, phone, email, password, confirm_password):
        name_field = self.obj.wait_till_present((By.XPATH, self.NAME_FIELD_XPATH))
        self.obj.send_k(name_field, name)

        address_field = self.obj.wait_till_present((By.XPATH, self.ADDRESS_FIELD_XPATH))
        self.obj.send_k(address_field, address)

        phone_field = self.obj.wait_till_present((By.XPATH, self.PHONE_FIELD_XPATH))
        self.obj.send_k(phone_field, phone)

        email_field = self.obj.wait_till_present((By.XPATH, self.EMAIL_FIELD_XPATH))
        self.obj.send_k(email_field, email)

        password_field = self.obj.wait_till_present((By.XPATH, self.PASSWORD_FIELD_XPATH))
        self.obj.send_k(password_field, password)

        password_confirmation_field = self.obj.wait_till_present((By.XPATH, self.PASSWORD_CONFIRMATION_FIELD_XPATH))
        self.obj.send_k(password_confirmation_field, confirm_password)

        signup_btn = self.obj.wait_till_clickable((By.XPATH, self.SIGNUP_BTN_XPATH))
        signup_btn.click()
