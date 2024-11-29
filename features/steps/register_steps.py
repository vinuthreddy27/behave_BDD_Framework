from behave import *
from features.POM.account_created_page import Account_creation
from features.POM.homepage import Homepage



@given(u'i navigated to register page')
def step_impl(context):
    context.homepage = Homepage(context.driver)
    context.Register_page=context.homepage.homepage_register()

@then(u'i validated the page title')
def step_impl(context):
    if context.driver.title=="Register Account":
        print("yes")

@then(u'i enter detail into name textfield')
def step_impl(context):
   context.Register_page.register("chris",
                        "rogers",
                        "rogers32@gmaill.com",
                        "999999999",
                        "aussie",
                        "aussie")

@then(u'i enter detail into  textfield')
def step_impl(context):

    context.Register_page.register2("ricky",
                          "ponting",
                          "ricky18@gmail.com",
                           "8888888888",
                          "sledging",
                          'sledging')

@then(u'i enter detail into firstname  textfield')
def step_impl(context):
    context.Register_page.register_3("vinuth")


@when(u'i clicked on submit button')
def step_impl(context):
   context.Account_creation.Register_page.submit_the_form()

@when(u'user should login successfully')
def step_impl(context):
    context.account_c_po=Account_creation(context.driver)
    context.account_c_po.message()

@when(u'user should get proper error message should display')

def step_impl(context):
    pass