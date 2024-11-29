from behave import *
from features.POM.loginpage import Loginpage


@when(u'i entered email  and password  into respective fields')
def step_impl(context):
    context.login_po=Loginpage(context.driver)
    context.login_po.login("reddyvinuth27@gmail.com",
                   "selenium")

@when(u'i entered product into search textfield')
def step_impl(context):
    context.ProductPage=context.homepage.Send_product("Imac")

@when(u'i clicked on add to cart btn')
def step_impl(context):
    context.ProductPage.btn()

@then(u'successfully product should be added to cart should display')
def step_impl(context):
  element=context.driver.find_element("xpath","//div[contains(@class,'alert')]")
  print(element.text)
  assert element.is_displayed()
