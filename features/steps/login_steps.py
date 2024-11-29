from behave import *
from features.POM.homepage import Homepage


@given(u'i navigated to login page')
def step_impl(context):

   context.homepage=Homepage(context.driver)
   context.Loginpage=context.homepage.homepage_login()

@when(u'i validate the title')
def step_impl(context):
    if context.driver.title=="Account Login":
        print("yes")
    print(context.driver.title)

@then(u'i enter valid credentials into respective textfield')
def step_impl(context):
       context.Loginpage.login("reddyvinuth27@gmail.com",
                   "selenium")

@then(u'user should login successfully')
def step_impl(context):
     context.Loginpage.conform_msg()


@then(u'i enter invalid credentials into respective textfield')
def step_impl(context):

    context.Loginpage.login("reddyvinuth27@gmail.com",
                           "selen")

@then(u'i enter email credential into respective textfield')
def step_impl(context):

    context.Loginpage.login("reddyvinuth27@gmail.com",
                    "")

@then(u'i enter password Credential into respective textfield')
def step_impl(context):
    context.Loginpage.login("",
                    "selenium")

@then(u'user should not  login successfully')
def step_impl(context):

    context.Loginpage.Warning_msg()


