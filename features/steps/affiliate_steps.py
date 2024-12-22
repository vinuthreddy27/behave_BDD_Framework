from behave import *
from features.POM.loginpage import Login_page

@when(u'i validated page title')
def step_impl(context):
    if context.driver.title=="Account Login":
        print("yes")
    else:
        print("no")

@when(u'i entered email and password into textfields')
def step_impl(context):
    context.login_page=Login_page(context.driver)
    context.landing_page=context.login_page.login("reddyvinuth27@gmail.com","selenium")


@when(u'i clicked on edit affiliate link')
def step_impl(context):
   context.affiliate_page=context.landing_page.edit_affiliate_account()


@when(u'do neceassary changes')
def step_impl(context):
    context.affiliate_page.modify()


@then(u'successfully changed message should display')
def step_impl(context):
    context.landing_page.display()
