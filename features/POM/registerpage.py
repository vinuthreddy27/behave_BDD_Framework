from features.POM.account_created_page import Account_creation
from features.library.lib import Base

class Register_page(Base):

    first_name_locator = ("id", "input-firstname")
    last_name_locator = ("id", "input-lastname")
    email_locator = ("id", "input-email")
    telephone_locator = ("id", "input-telephone")
    password_locator = ("id", "input-password")
    conform_password_locator = ("id", "input-confirm")
    radio_btn = ("xpath", "//label[@class='radio-inline']/input[@value = '1']")
    privacy_policy_check_box_btn = ("xpath", "//input[@type='checkbox']")
    register_btn = ("xpath", "//input[@value='Continue']")

    def register(self,fn,ln,mail,pno,password,c_password):
        self.Send_keys(self.first_name_locator,fn)
        self.Send_keys(self.last_name_locator,ln)
        self.Send_keys(self.email_locator,mail)
        self.Send_keys(self.telephone_locator,pno)
        self.Send_keys(self.password_locator,password)
        self.Send_keys(self.conform_password_locator,c_password)
        self.Click(self.radio_btn)
        self.Click(self.privacy_policy_check_box_btn)

        return Account_creation(self.driver)

    def register2(self,fn,ln,mail,pno,password,c_password):
        self.Send_keys(self.first_name_locator,fn)
        self.Send_keys(self.last_name_locator,ln)
        self.Send_keys(self.email_locator,mail)
        self.Send_keys(self.telephone_locator,pno)
        self.Send_keys(self.password_locator,password)
        self.Send_keys(self.conform_password_locator,c_password)
        self.Click(self.privacy_policy_check_box_btn)

    def register_3(self,fn):
        self.Send_keys(self.first_name_locator,fn)

    def register_4(self, ln):
        self.Send_keys(self.last_name_locator, ln)

    def register_5(self, email):
        self.Send_keys(self.email_locator, email)

    def register_6(self, phno):
        self.Send_keys(self.telephone_locator, phno)

    def register_7(self, password):
        self.Send_keys(self.password_locator,password)

    def submit_the_form(self):
        self.Submit(self.password_locator)

