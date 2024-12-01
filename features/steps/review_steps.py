from behave import *

@when(u'i entered valid credentials into email and password fields')
def step_impl(context):
   context.login_page.login("reddyvinuth27@gmail.com","selenium")



@when(u'i searched ipod touch product')
def step_impl(context):
    context.product_page=context.homepage.Send_product("ipod touch")

@when(u'i clicked on review link and added my review')
def step_impl(context):
    context.review_page=context.product_page.click_product_link()
    context.review_page.add_a_review("chris","....................................................................................")


@then(u'successfully message should display')
def step_impl(context):
    context.review_page.dispaly_success_msg()


@then(u'i clicked on review link and added my review in words less then 25')
def step_impl(context):
  context.review_page = context.product_page.click_product_link()
  context.review_page.add_a_review("bumraah","happy birthday to you")


@then(u'proper message should display')
def step_impl(context):
    context.review_page.display_errormsg()
