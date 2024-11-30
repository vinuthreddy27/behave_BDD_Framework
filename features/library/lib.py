import time
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def generate_random_email(self):
        timestamp = time.ctime().split()[3]
        timestamp1 = timestamp.replace(":", "")
        return "vinuth" + timestamp1 + "@gmail.com"

    def search_for_an_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def Click(self, locator):
        element = self.search_for_an_element(locator)
        element.click()

    def Send_keys(self, locator, text):
        element = self.search_for_an_element(locator)
        element.clear()
        element.send_keys(text)

    def Submit(self, locator):
        element = self.search_for_an_element(locator)
        element.submit()

    def Display_status(self,locator):
        element=self.search_for_an_element(locator)
        return element.is_displayed()

    def print_text(self, locator):
        element = self.search_for_an_element(locator)
        print(element.text)

    def wait_for_visibility(self,locator,timeout):
        wait=WebDriverWait(self.driver,timeout)
        condition=visibility_of_element_located(locator)
        element=wait.until(condition)
        return element

    def verify_radiobtn(self,locator):
        element=self.search_for_an_element(locator)
        print(element.is_selected())
        return element.is_selected()

    def verify_checkbox(self, locator):
        element = self.search_for_an_element(locator)
        print(element.is_selected())
        return element.is_selected()

