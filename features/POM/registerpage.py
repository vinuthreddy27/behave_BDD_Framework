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

    def register(self,fn,ln,pno,password,c_password):
        self.Send_keys(self.first_name_locator,fn)
        self.Send_keys(self.last_name_locator,ln)
        self.Send_keys(self.email_locator,self.generate_random_email())
        self.Send_keys(self.telephone_locator,pno)
        self.Send_keys(self.password_locator,password)
        self.Send_keys(self.conform_password_locator,c_password)
        self.Click(self.radio_btn)
        self.Click(self.privacy_policy_check_box_btn)


    def submit_the_form(self):
        self.Submit(self.password_locator)

        return Account_creation(self.driver)

