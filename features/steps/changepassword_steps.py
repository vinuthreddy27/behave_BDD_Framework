from behave import *

from features.POM.landing_page import Landing_page


@when(u'i click on change password link')
def step_impl(context):
   context.landing_obj=Landing_page(context.driver)


@when(u'do necessary changes')
def step_impl(context):
    raise NotImplementedError(u'STEP: When do necessary changes')


@then(u'password changed message should dispaly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then password changed message should dispaly')
