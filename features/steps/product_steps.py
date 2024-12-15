from behave import *
from features.POM.homepage import Homepage


@given(u'i navigated to homepage')
def step_impl(context):
    context.homepage=Homepage(context.driver)
    context.login_page=context.homepage.homepage_login()

@then(u'i login with valid credentials')
def step_impl(context):

    context.login_page.login("reddyvinuth27@gmail.com",
                        "selenium")

@then(u'i entered {product} into searchtextfield')
def step_impl(context,product):

    context.ProductPage=context.homepage.Send_product(product)

@then(u'product should display')
def step_impl(context):
   assert context.ProductPage.get_message()


@then(u'no product message should display')
def step_impl(context):
    assert context.ProductPage.no_message()




