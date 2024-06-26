from selenium.webdriver.common.by import By

from base.base_code import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.LOGIN_BTN_XPATH = "//a[contains(text(), 'Login')]"
        self.SERVICE_BTN_XPATH = "//a[text()='Service']"
        self.LOGOUT_BTN_XPATH = "//button[text()='Log Out']"
        self.MY_SERVICES_BTN = (By.XPATH, "//button[text()='My services']")
        self.SELECT_SERVICE_BTN = (By.XPATH, '//*[@id="skill_type"]')
        self.FLASH_CLOSE_BTN = (By.XPATH, '//button[@class="btn-close"]')
        self.PROFILE_BTN_XPATH = '//button[text()="Profile"]'
        self.DASHBOARD_BTN_XPATH = '//a[text()="Dashboard"]'
        self.PENDING_REQUESTS_BTN_XPATH = "//button[text()='Pending requests']"

    def login_btn_click(self):
        login_btn = self.wait_till_present((By.XPATH, self.LOGIN_BTN_XPATH))
        login_btn.click()

    def service_btn_click(self):
        service_btn = self.wait_till_present((By.XPATH, self.SERVICE_BTN_XPATH))
        service_btn.click()

    def logout(self):
        logout_btn = self.wait_till_present((By.XPATH, self.LOGOUT_BTN_XPATH))
        logout_btn.click()

    def my_services(self):
        my_services_btn = self.wait_till_clickable(self.MY_SERVICES_BTN)
        my_services_btn.click()

    def profile(self):
        profile_btn = self.wait_till_clickable((By.XPATH, self.PROFILE_BTN_XPATH))
        profile_btn.click()

    def services(self):
        select_service_btn = self.wait_till_present(self.SELECT_SERVICE_BTN)
        select_service_btn.click()

    def close_flash(self):
        flash_close_btn = self.wait_till_clickable(self.FLASH_CLOSE_BTN)
        flash_close_btn.click()

    def admin_dashboard(self):
        dashboard_btn = self.wait_till_clickable((By.XPATH, self.DASHBOARD_BTN_XPATH))
        dashboard_btn.click()

    def pending_requests(self):
        pending_requests_btn = self.wait_till_clickable((By.XPATH, self.PENDING_REQUESTS_BTN_XPATH))
        pending_requests_btn.click()
