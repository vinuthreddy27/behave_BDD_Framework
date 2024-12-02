from features.POM.changepassword_page import Password_change_page
from features.POM.edit_affiliatePage import Edit_affiliate
from features.POM.modify_accountpage import Modify_account
from features.POM.registerpage import Register_page
from features.library.lib import Base


class Landing_page(Base):
    edit_link = ("xpath", "//a[.='Edit your account information']")
    change_password_locator = ("xpath", "//ul[@class='list-unstyled']/..//a[.='Change your password']")
    A_account_link = ("xpath", "//a[.='Edit your affiliate information']")
    success_pass_changed = ("xpath", "//*[.='Success: Your password has been successfully updated.']")
    register_link=("link text","Register")
    affiilate_msg=("xpath","//*[.='Success: Your account has been successfully updated.']")

    def edit_account_info(self):
        self.Click(self.edit_link)

        return Modify_account(self.driver)

    def change_password(self):
        self.Click(self.change_password_locator)

        return Password_change_page(self.driver)

    def edit_affiliate_account(self):
        self.Click(self.A_account_link)

        return Edit_affiliate(self.driver)

    def password_changed(self):
        self.print_text(self.success_pass_changed)
        return self.Display_status(self.success_pass_changed)

    def display(self):
        self.print_text(self.affiilate_msg)
        self.Display_status(self.affiilate_msg)


    def click_register(self):
        self.Click(self.register_link)
        return Register_page(self.driver)