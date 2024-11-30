from features.library.lib import Base

class Subscription_page(Base):
    yes=("xpath","//input[@value='1']")
    no=("xpath","//input[@value='0']")


    def Yes(self):
        self.Click(self.yes)

    def No(self):
        self.Click(self.no)

    def validate_yes(self):
         return self.verify_radiobtn(self.yes)

    def validate(self):
         return self.verify_radiobtn(self.no)