from features.POM.loginpage import Loginpage
from features.POM.product_page import ProductPage
from features.POM.registerpage import Register_page
from features.library.lib import Base


class Homepage(Base):

    my_account_locator = ("xpath", "//span[.='My Account']")
    register_locator = ("xpath", "//a[.='Register']")
    login_locator=("xpath","//a[.='Login']")
    search_tf=("name","search")
    btn=("css selector","span[class='input-group-btn']")
    wishlist=("xpath","//span[.='Wish List (1)']")

    def homepage_register(self):
        self.Click(self.my_account_locator)
        self.Click(self.register_locator)

        return Register_page(self.driver)

    def homepage_login(self):
        self.Click(self.my_account_locator)
        self.Click(self.login_locator)

        return Loginpage(self.driver)

    def Send_product(self,product):
        self.Send_keys(self.search_tf,product)
        self.Click(self.btn)

        return ProductPage(self.driver)


    def wish_list(self):
        self.Click(self.wishlist)

        return ProductPage(self.driver)
