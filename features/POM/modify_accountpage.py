from features.library.lib import Base


class Modify_account(Base):
    telephone_locator = ("name", "telephone")
    continue_btn = ("xpath", "//input[@value='Continue']")


    def modify(self,phno):
     self.Send_keys(self.telephone_locator, phno)
     self.Click(self.continue_btn)

