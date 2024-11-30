from features.library.lib import Base


class Edit_affiliate(Base):

    company_text_field = ("name", "company")
    website_textfield = ("name", "website")
    tax_textfield = ("name", "tax")
    payment_mode_btn = ("xpath", "//input[@value='paypal']")
    paypal_textfield = ("name", "paypal")
    continue_btn = ("xpath", "//input[@type='submit']")

    def edit_affiliate(self,company_name,website,tax,pay):
        self.Send_keys(self.company_text_field,company_name)
        self.Send_keys(self.website_textfield,website)
        self.Send_keys(self.tax_textfield,tax)
        self.Click(self.payment_mode_btn)
        self.Send_keys(self.paypal_textfield,pay)
        self.Click(self.continue_btn)



