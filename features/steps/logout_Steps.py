from  behave import *


@when(u'i validate page title')
def step_impl(context):
    if context.driver.title == "Account Login":
        print("yes")
    print(context.driver.title)

@when(u'i clicked on logout link')
def step_impl(context):
    context.logout_page=context.homepage.click_on_logout()

@then(u'proper message should display on logout')
def step_impl(context):
    context.logout_page.dispaly_success_logout()

