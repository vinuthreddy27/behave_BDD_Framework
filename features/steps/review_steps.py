from behave import *
from features.POM.loginpage import Loginpage


@when(u'i enterd valid credentials into email and password fields')
def step_impl(context):
   context.loginp_obj=Loginpage(context.driver)
   context.loginp_obj.login("reddyvinuth27@gmail.com","selenium")


@when(u'i clicked on login button')
def step_impl(context):
    context.loginp_obj.click_on_login()


@when(u'i searched ipod touch product')
def step_impl(context):
    context.Product_page=context.homepage.Send_product("ipod touch")


@when(u'i clicked on review link and added my review')
def step_impl(context):
   context.Review_page=context.Product_page.click_product_link()
   context.Review_page.add_a_review("vinuthreddy","hello good morning.......................................................................")

@then(u'successfull message should display')
def step_impl(context):
    context.Review_page.dispaly_success_msg()
