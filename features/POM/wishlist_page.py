from features.library.lib import Base


class wishlist_page(Base):
    remove_btn=("xpath","//a[@class='btn btn-danger']")
    message=("xpath","//div[@class='alert alert-success alert-dismissible']")

    def click_remove_btn(self):
        self.Click(self.remove_btn)

    def proper_message(self):
        self.print_text(self.message)
        self.Display_status(self.message)