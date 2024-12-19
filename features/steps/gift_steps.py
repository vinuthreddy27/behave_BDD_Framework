

from behave import *

from features.POM.homepage import Homepage


@given(u'i nagigated to login page')
def step_impl(context):
  context.homepage=Homepage(context.driver)
  context.login_page=context.homepage.homepage_login()

@when(u'i enter valid credentials into respective textfield')
def step_impl(context):
    context.login_page.login("reddyvinuth27@gmail.com", "selenium")

@when(u'i clicked on gift cerficates')
def step_impl(context):
   context.gift_page=context.homepage.click_giftlink()

@when(u'enter all the credentials into fields')
def step_impl(context):
    context.gift_page.gift("chris","rogers@gmail.com","......................................................................","3")


@then(u'gift sent successfully message should display')
def step_impl(context):
    context.gift_page.get_message()
