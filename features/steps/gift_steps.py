from time import sleep
from behave import *
from features.POM.gift_page import Gift_page
from features.POM.homepage import Homepage


@given(u'i nagigated to login page')
def step_impl(context):
  context.homepage=Homepage(context.driver)
  context.Loginpage=context.homepage.homepage_login()

@when(u'i enter valid credentials into respective textfield')
def step_impl(context):
    context.Loginpage.login("reddyvinuth27@gmail.com", "selenium")

@when(u'i clicked on gift cerficates')
def step_impl(context):
   context.Gift_page=context.homepage.click_giftlink()

@when(u'enter all the credentials into fields')
def step_impl(context):
    context.Gift_page.gift("chris","rogers",".......","3")

@then(u'gift sent successfully message should display')
def step_impl(context):
    pass