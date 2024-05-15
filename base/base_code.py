from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def implicit_wait(self, sec=7):
        self.driver.implicitly_wait(sec)

    def wait_till_present(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))

    def wait_till_all_present(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.presence_of_all_elements_located(locator))

    def wait_till_clickable(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator))

    def send_k(self, element, data):
        element.send_keys(data)
