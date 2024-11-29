
from behave import *
from features.POM.homepage import Homepage


@given(u'i navigated to the homepage')
def step_impl(context):
    context.homepage=Homepage(context.driver)
    context.Loginpage=context.homepage.homepage_login()

@then(u'i validated page title')
def step_impl(context):
    if context.driver.title=="Account Login":
        print("yes")
    else:
        print("no")

@then(u'i entered email and password into textfields')
def step_impl(context):
    context.Loginpage.login("reddyvinuth@27@gmail.com",
                            "selenium")


@then(u'i entered a product name into respective field')
def step_impl(context):
   context.homepage=context.homepage.Send_product("Iphone")

@then(u'i clicked on the wishlist btn')
def step_impl(context):
    pass

@then(u'i submit the form')
def step_impl(context):
    pass