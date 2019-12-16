from .base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def validate_page(self):
        self.wait_until_page_is_not_loading()
        assert self.driver.title == 'PHPTRAVELS | Travel Technology Partner'

    
