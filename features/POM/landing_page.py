from features.library.lib import Base


class Landing_page(Base):
    edit_link = ("xpath", "//a[.='Edit your account information']")
    change_password_locator = ("xpath", "//ul[@class='list-unstyled']/..//a[.='Change your password']")
    A_account_link = ("xpath", "//a[.='Edit your affiliate information']")

    def edit_account_info(self):
        self.Click(self.edit_link)

        # return Modify_account(self.driver)

    def change_password(self):
        self.Click(self.change_password_locator)

        # return Password_change_page(self.driver)

    def edit_affiliate_account(self):
        self.Click(self.A_account_link)

        # return Edit_affiliate(self.driver)
