import allure
from selenium import webdriver
from configurations.config import TestData


def before_scenario(context,driver):

    browser=TestData.browser
    if browser.__eq__("chrome"):
        context.driver=webdriver.Chrome()

    elif browser.__eq__("firefox"):
        context.driver=webdriver.Firefox()

    elif browser.__eq__("edge"):
        context.driver=webdriver.Edge()

    else:
        print("provide valid browser")

    context.driver.implicitly_wait(3)
    context.driver.get(TestData.base_url)
    context.driver.maximize_window()

def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    print()
    if step.status=="failed":
        allure.attach(context.driver.get_screenshot_as_png(),name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


