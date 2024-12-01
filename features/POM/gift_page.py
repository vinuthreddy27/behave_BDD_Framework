from features.library.lib import Base


class Gift_page(Base):

    receipient_locator=("id","input-to-name")
    receipient_email=("id","input-to-email")
    your_name=("id","input-from-name")
    your_email=("id","input-from-email")
    birthday_btn=("xpath","//input[@value='7']")
    message=("xpath","//textarea[@id='input-message']")
    amount=("xpath","//input[@name='amount']")
    agree_checkbox=("xpath","//input[@name='agree']")
    continue_btn=("xpath","//input[@value='Continue']")

    proper_message=("xpath","//p[contains(.,'Thank you for purchasing a gift certificate!')]")


    def gift(self,name,mail,msg,amnt):
        self.Send_keys(self.receipient_locator,name)
        self.Send_keys(self.receipient_email,mail)

        self.Click(self.birthday_btn)
        self.Send_keys(self.message,msg)
        self.Send_keys(self.amount,amnt)
        self.Click(self.agree_checkbox)
        self.Click(self.continue_btn)

    def get_message(self):
        self.print_text(self.proper_message)
        self.Display_status(self.proper_message)