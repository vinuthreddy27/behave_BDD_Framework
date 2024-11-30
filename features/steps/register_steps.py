from time import sleep

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
                        "999999999",
                        "aussie",
                        "aussie")

@when(u'i clicked on submit button')
def step_impl(context):
     context.Account_creation=context.Register_page.submit_the_form()

@when(u'user should login successfully')
def step_impl(context):
   context.Account_creation.success_msg()
