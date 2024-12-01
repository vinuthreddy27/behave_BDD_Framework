from behave import *

from features.POM.landing_page import Landing_page


@then(u'i clicked on edit affiliate link')
def step_impl(context):
    context.landing_page=Landing_page(context.driver)
    context.affiliate_page=context.landing_page.edit_affiliate_account()

@then(u'do neceassary changes')
def step_impl(context):
   context.affiliate_page.modify()


@then(u'successfully changed message should display')
def step_impl(context):
  context.landing_page.display()
