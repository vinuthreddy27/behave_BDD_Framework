from behave import *
from features.POM.homepage import Homepage


@given(u'i navigated to the homepage')
def step_impl(context):
    context.homepage=Homepage(context.driver)
    context.login_page=context.homepage.homepage_login()

@then(u'i validated page title')
def step_impl(context):
    if context.driver.title=="Account Login":
        print("yes")
    else:
        print("no")

@then(u'i entered email and password into textfields')
def step_impl(context):
    context.login_page.login("reddyvinuth27@gmail.com",
                            "selenium")

@then(u'i entered a product name into respective field')
def step_impl(context):
   context.product_page=context.homepage.Send_product("Iphone")

@then(u'i clicked on the wishlist btn')
def step_impl(context):

   context.product_page.wishlist_link()

@then(u'product should be added to wishlist')
def step_impl(context):

  context.product_page.get_text()


@then(u'i clik on wishlist and remove product from wishlist')
def step_impl(context):
   context.wishlist_Page=context.homepage.wish_link()
   context.wishlist_Page.click_remove_btn()

@then(u'product should be removed from  wishlist')
def step_impl(context):

    context.wishlist_Page.proper_message()


