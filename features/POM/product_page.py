from features.POM.review_page import Review_page
from features.POM.wishlist_page import wishlist_page
from features.library.lib import Base


class ProductPage(Base):

    product_link = ("link text", "iPod Touch")
    review_link = ("xpath", "//a[.='Write a review']")
    cart_btn=("xpath","//span[.='Add to Cart']")
    wishlist_btn=("css selector","button[data-original-title='Add to Wish List']")
    message=("xpath","//div[contains(@class,'alert')]")
    no_Product_match=("xpath","//p[.='There is no product that matches the search criteria.']")
    product_match=("xpath","//h2[.='Products meeting the search criteria']")

    def btn(self):
        self.Click(self.cart_btn)

    def message_(self):
        self.Display_status(self.message)

    def wishlist_link(self):
        self.Click(self.wishlist_btn)

    def click_product_link(self):
        self.Click(self.product_link)
        self.Click(self.review_link)

        return Review_page(self.driver)

    def get_text(self):
        self.print_text(self.message)
        self.Display_status(self.message)

        return wishlist_page(self.driver)

    def get_message(self):
        self.print_text(self.product_match)
        self.Display_status(self.product_match)

    def no_message(self):
        self.print_text(self.no_Product_match)
        self.Display_status(self.no_Product_match)
