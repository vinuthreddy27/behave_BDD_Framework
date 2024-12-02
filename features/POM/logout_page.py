from features.library.lib import Base

class Logout_page(Base):
    message=("xpath","//p[.='You have been logged off your account. It is now safe to leave the computer.']")


    def dispaly_success_logout(self):
        self.print_text(self.message)
        self.Display_status(self.message)