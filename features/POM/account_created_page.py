from features.library.lib import Base


class Registered_success(Base):

    message=("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']")

    def success_msg(self):
        self.print_text(self.message)
        self.Display_status(self.message)

