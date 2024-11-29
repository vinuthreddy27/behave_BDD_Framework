from behave import *
from features.POM.homepage import Homepage
from features.POM.loginpage import Loginpage


@given(u'i navigated to homepage')
def step_impl(context):
    homepage_obj=Homepage(context.driver)
    homepage_obj.homepage_login()

@then(u'i login with valid credentials')
def step_impl(context):
    login_pageobj=Loginpage(context.driver)
    login_pageobj.login("reddyvinuth27@gmail.com",
                        "selenium")

@then(u'i entered {product} into searchtextfield')
def step_impl(context,product):
    homepage_obj = Homepage(context.driver)
    homepage_obj.Send_product(product)

@then(u'product should display')
def step_impl(context):
    pass
    # assert context.driver.find_element("xpath","//p[.='There is no product that matches the search criteria.']").is_displayed()



