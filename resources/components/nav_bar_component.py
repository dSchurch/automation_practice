from .base_component import BaseComponent


class NavBarComponent(BaseComponent):

    _nav_bar_page_logo_selector = "[alt='PHPTRAVELS | Travel Technology Partner']"

    def __init__(self, driver):

        super().__init__(driver)
    
    def click_page_logo(self):

        logoElement = self.driver.find_element_by_css_selector(self._nav_bar_page_logo_selector)
        logoElement.click()
