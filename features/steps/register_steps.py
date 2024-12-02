
from behave import *
from features.POM.homepage import Homepage


@given(u'i navigated to register page')
def step_impl(context):
    context.homepage = Homepage(context.driver)
    context.register_page=context.homepage.homepage_register()

@then(u'i validated the page title')
def step_impl(context):
    if context.driver.title=="Register Account":
        print("yes")

@then(u'i enter detail into name textfield')
def step_impl(context):
   context.register_page.register("chris",
                        "rogers",
                        "999999999",
                        "aussie",
                        "aussie")

@when(u'i clicked on submit button')
def step_impl(context):
     context.registered_page=context.register_page.submit_the_form()

@when(u'user should login successfully')
def step_impl(context):
   context.registered_page.success_msg()


@when(u'i clicked on continue btn')
def step_impl(context):
    context.homepage_obj=Homepage(context.driver)
    context.login_page=context.homepage_obj.homepage_login()
    context.login_page.click_on_continue()


@then(u'register page should display')
def step_impl(context):
    if context.driver.title == "Register Account":
        print("yes")
    print(context.driver.title)

@then(u'i clicked on register link')
def step_impl(context):
    context.login_page=context.homepage.homepage_login()
    context.landing_page=context.login_page.login("reddyvinuth27@gmail.com","selenium")
    context.landing_page.click_register()