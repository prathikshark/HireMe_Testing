from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def login_btn_click(self):
        login_btn = self.obj.wait_till_visible((By.XPATH, "//a[contains(text(), 'Login')]"))
        login_btn.click()

    def register_as_customer(self):
        name_field = self.obj.wait_till_present((By.XPATH, "// input[ @ id = 'user_name']"))
        self.obj.send_k(name_field, 'Prathiksha')

        address_field = self.obj.wait_till_present((By.XPATH, "// input[@id='user_address']"))
        self.obj.send_k(address_field, 'marathalli')

        phone_field = self.obj.wait_till_present((By.XPATH, "// input[@id='user_phone']"))
        self.obj.send_k(phone_field, '1234567890')

        email_field = self.obj.wait_till_present((By.XPATH, "// input[@id='user_email']"))
        self.obj.send_k(email_field, 'prathiksha566@gmail.com')

        password_field = self.obj.wait_till_present((By.XPATH, "// input[@id='user_password']"))
        self.obj.send_k(password_field, '111111')

        password_confirmation_field = self.obj.wait_till_present((By.XPATH, "// input[@id='user_password_confirmation']"))
        self.obj.send_k(password_confirmation_field, '111111')

        signup_btn = self.obj.wait_till_clickable((By.XPATH, "//input[@id='submit-btn']"))
        signup_btn.click()
