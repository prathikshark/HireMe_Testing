from selenium.webdriver.common.by import By
from base.base_code import BaseClass
import time

class BookingsPage:
    REMOVE_SERVICE_BTN = (By.XPATH, "(//button[text()=' Remove'])[1]")
    BOOK_BTN = (By.XPATH, "//button[contains(text(), 'Book')]")
    CONFIRM_BTN = (By.XPATH, '//button[text()="Confirm"]')

    def __init__(self, driver):
        self.driver = driver
        self.obj = BaseClass(self.driver)

    def remove_service(self):
        remove_service_btn = self.obj.wait_till_clickable(self.REMOVE_SERVICE_BTN)
        remove_service_btn.click()

    def book(self):
        book_btn = self.obj.wait_till_clickable(self.BOOK_BTN)
        booking_id = book_btn.get_attribute("data-booking-id")
        book_btn.click()
        return booking_id

    def confirm(self):
        confirm_btn = self.obj.wait_till_clickable(self.CONFIRM_BTN)
        confirm_btn.click()
