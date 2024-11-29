
class Base:

    def __init__(self, driver):
        self.driver = driver

    def search_for_an_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def Click(self, locator):
        element = self.search_for_an_element(locator)
        element.click()

    def Send_keys(self, locator, text):
        element = self.search_for_an_element(locator)
        element.send_keys(text)

    def Submit(self, locator):
        element = self.search_for_an_element(locator)
        element.submit()

    def Display_status(self,locator):
        element=self.search_for_an_element(locator)
        return element.is_displayed()