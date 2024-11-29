from features.library.lib import Base


class Account_creation(Base):

    message=("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']")

    def success_msg(self):
        element=self.search_for_an_element(self.message)
        return element.is_displayed()
