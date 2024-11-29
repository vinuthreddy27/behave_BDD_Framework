from features.library.lib import Base


class ProductPage(Base):

    cart_btn=("xpath","//span[.='Add to Cart']")
    wishlist_btn=("css selector","button[data-original-title='Add to Wish List']")
    message=("xpath","//div[contains(@class,'alert')]")

    def btn(self):
        self.Click(self.cart_btn)

    def message_(self):
        self.Display_status(self.message)

    def wishlist_link(self):
        self.Click(self.wishlist_btn)
        