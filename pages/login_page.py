from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):

    def go_to_test_suit_page(self):
        login_box = self.driver.find_element(By.NAME, 'name')
        login_box.clear()
        login_box.send_keys('qa.osinit@gmail.com')
        password_box = self.driver.find_element(By.NAME, 'password')
        password_box.clear()
        password_box.send_keys('QA.osinit')
        button = self.driver.find_element(By.CLASS_NAME, 'loginpage-button-sso-disable')
        button.click()
