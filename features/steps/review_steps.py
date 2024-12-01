from behave import *
from features.POM.homepage import Homepage


@when(u'i enterd valid credentials into email and password fields')
def step_impl(context):

  context.login_page.login("reddyvinuth27@gmail.com","selenium")


@when(u'i clicked on login button')
def step_impl(context):
    context.login_page.submit_the_form()


@when(u'i searched ipod touch product')
def step_impl(context):
    context.homepage=Homepage(context.driver)
    context.product_Page=context.homepage.Send_product("ipod touch")


@when(u'i clicked on review link and added my review')
def step_impl(context):
   context.review_page=context.product_Page.click_product_link()
   context.review_page.add_a_review("vinuthreddy","hello good morning.......................................................................")

@then(u'successfull message should display')
def step_impl(context):
    context.review_page.dispaly_success_msg()
