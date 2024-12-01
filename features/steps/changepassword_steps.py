from behave import *
from features.POM.landing_page import Landing_page


@when(u'i click on change password link')
def step_impl(context):
   context.landing_page=Landing_page(context.driver)
   context.password_page=context.landing_page.change_password()


@when(u'do necessary changes')
def step_impl(context):
   context.password_page.change("selenium","selenium")


@then(u'password changed message should dispaly')
def step_impl(context):
   context.landing_page.password_changed()