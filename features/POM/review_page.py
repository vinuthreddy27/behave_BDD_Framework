from features.library.lib import Base


class Review_page(Base):
    yourname_tf = ("id", "input-name")
    text_area = ("name", "text")
    rating_rb = ("xpath", "//input[@value='5']")
    continue_btn = ("id", "button-review")
    warning_msgg=("xpath","//div[contains(@class,'alert')]")
    success_msg=("xpath","//*[.=' Thank you for your review. It has been submitted to the webmaster for approval.']")
    def add_a_review(self,yourname,text):
        self.Send_keys(self.yourname_tf,yourname)
        self.Send_keys(self.text_area,text)
        self.Click(self.rating_rb)
        self.Click(self.continue_btn)

    def dispaly_success_msg(self):
        self.print_text(self.success_msg)
        self.Display_status(self.warning_msgg)

    def display_errormsg(self):
        self.print_text(self.warning_msgg)
        self.Display_status(self.warning_msgg)
