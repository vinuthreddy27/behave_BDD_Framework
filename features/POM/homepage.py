from features.POM.gift_page import Gift_page
from features.POM.loginpage import  Login_page
from features.POM.logout_page import  Logout_page
from features.POM.product_page import ProductPage
from features.POM.registerpage import Register_page
from features.POM.wishlist_page import wishlist_page
from features.library.lib import Base


class Homepage(Base):

    my_account_locator = ("xpath", "//span[.='My Account']")
    register_locator = ("xpath", "//a[.='Register']")
    login_locator=("xpath","//a[.='Login']")

    search_tf=("name","search")
    btn=("css selector","span[class='input-group-btn']")

    wishlist=("xpath","//span[.='Wish List (1)']")

    logout_btn = ("xpath", "//ul[@class='dropdown-menu dropdown-menu-right']/..//a[.='Logout']")

    gift_locator = ("xpath", "//a[.='Gift Certificates']")

    contact_us_locator = ("xpath", "//a[.='Contact Us']")

    cart_link = ("id", "wishlist-total")

    cart_total = ("css selector", "*[id='cart']")
    shopping_cart = ("css selector", "a[title='Shopping Cart']")
    downloads_link = ("xpath", "//li[@class='dropdown']//li[.='Downloads']")
    transactions_link = ("xpath", "//li[@class='dropdown']//li[.='Transactions']")
    order_history_link = ("xpath", "//li[@class='dropdown']//li[.='Order History']")
    logout_link = ("xpath", "//ul[starts-with(@class,'dropdown')]//a[.='Logout']")

    def homepage_register(self):
        self.Click(self.my_account_locator)
        self.Click(self.register_locator)

        return Register_page(self.driver)

    def homepage_login(self):
        self.Click(self.my_account_locator)
        self.Click(self.login_locator)

        login_page=Login_page(self.driver)

        return login_page

    def Send_product(self,product):
        self.Send_keys(self.search_tf,product)
        self.Click(self.btn)

        return ProductPage(self.driver)


    def wish_list(self):
        self.Click(self.wishlist)

        return ProductPage(self.driver)


    def click_giftlink(self):
        self.Click(self.gift_locator)

        return Gift_page(self.driver)

    def wish_link(self):
        self.Click(self.wishlist)

        return wishlist_page(self.driver)


    def click_on_logout(self):
        self.Click(self.my_account_locator)
        self.Click(self.logout_link)

        return Logout_page(self.driver)