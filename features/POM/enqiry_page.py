
from features.library.lib import Base


class Enquiry_page(Base):
    text_area_locator=("name","enquiry")
    name=("name","name")
    email=("name","email")
    submit_btn=("xpath","//input[@value='Submit']")
    continue_btn3=("xpath","//a[.='Continue']")


    def enquiry(self,name,mail,text):
        self.Send_keys(self.name, name)
        self.Send_keys(self.email,mail)
        self.Send_keys(self.text_area_locator,text)
        self.Click(self.submit_btn)
        self.Click(self.continue_btn3)