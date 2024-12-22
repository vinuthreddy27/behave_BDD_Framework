from features.POM.landing_page import Landing_page
from features.POM.registerpage import Register_page
from features.library.lib import Base


class Login_page(Base):
    continue_btn=("link text","Continue")

    email_locator = ("id", "input-email")
    password_locator = ("id", "input-password")
    login_btn = ("xpath", "//input[@value='Login']")
    warning_message=("xpath","//div[.='Warning: No match for E-Mail Address and/or Password.']")
    conform_message=("xpath", "//li[.='Change your password']")

    def login(self,email,password):
        self.Send_keys(self.email_locator,email)
        self.Send_keys(self.password_locator,password)
        self.Click(self.login_btn)

        landing_page=Landing_page(self.driver)
        return landing_page


    def submit_the_form(self):
        self.Submit(self.email_locator)

    def Warning_msg(self):
      self.Display_status(self.warning_message)

    def conform_msg(self):
     self.Display_status(self.conform_message)


    def click_on_continue(self):
        self.Click(self.continue_btn)

        return Register_page(self.driver)
