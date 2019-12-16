from .base_component import BaseComponent


class NavBarComponent(BaseComponent):

    nav_bar_page_logo_locator = "[alt='PHPTRAVELS | Travel Technology Partner']"
    currency_dropdown_locator = ".dropdown-currency"

    def __init__(self, driver):

        super().__init__(driver)
    
    def click_page_logo(self):

        logoElement = self.driver.find_element_by_css_selector(self.nav_bar_page_logo_locator)
        logoElement.click()

    def open_currency_dropdown(self):
        currencyDropdownElement = self.driver.find_element_by_css_selector(self.currency_dropdown_locator)
        currencyDropdownElement.click()

    


