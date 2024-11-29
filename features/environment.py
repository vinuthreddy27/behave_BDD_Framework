import allure
from selenium import webdriver
from utilites import configReader

def before_scenario(context,driver):
    browser_name=configReader.read_configuration("basic info","browser")
    if browser_name.__eq__("chrome"):
        context.driver=webdriver.Chrome()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    else:
        print("invalid browser")
    context.driver.implicitly_wait(10)
    context.driver.get(configReader.read_configuration("basic info","url"))
    context.driver.maximize_window()

def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    print()
    if step.status=="failed":
        allure.attach(context.driver.get_screenshot_as_png(),name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


