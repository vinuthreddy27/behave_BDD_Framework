from features.POM.landing_page import Landing_page
from features.library.lib import Base


class Loginpage(Base):

    email_locator = ("id", "input-email")
    password_locator = ("id", "input-password")
    login_btn = ("xpath", "//input[@value='Login']")
    warning_message=("xpath","//div[.='Warning: No match for E-Mail Address and/or Password.']")
    conform_message=("xpath", "//li[.='Change your password']")

    def login(self,email,password):
        self.Send_keys(self.email_locator,email)
        self.Send_keys(self.password_locator,password)
        self.Click(self.login_btn)

        return Landing_page(self.driver)

    def click_on_login(self):
        self.Click(self.login_btn)

    def Warning_msg(self):
      self.Display_status(self.warning_message)

    def conform_msg(self):
     self.Display_status(self.conform_message)
