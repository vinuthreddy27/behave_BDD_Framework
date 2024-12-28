from behave import *
from features.POM.loginpage import Login_page
from features.POM.wishlist_page import wishlist_page


@when(u'i entered email  and password  into respective fields')
def step_impl(context):
    context.login_page=Login_page(context.driver)
    context.login_page.login("reddyvinuth27@gmail.com",
                   "selenium")

@when(u'i entered product into search textfield')
def step_impl(context):
    context.productPage=context.homepage.Send_product("Imac")

@when(u'i clicked on add to cart btn')
def step_impl(context):
    context.productPage.btn()

@then(u'successfully product should be added to cart should display')
def step_impl(context):
  context.productPage.get_text()


@then(u'i clicked on  cart link')
def step_impl(context):
   context.homepage.wish_link()


@then(u'i clicked on remove btn')
def step_impl(context):
    context.wish_page=wishlist_page(context.driver)
    context.wish_page.click_remove_btn()


@then(u'then product  should be removed from cart should display')
def step_impl(context):
   context.wish_page.proper_message()