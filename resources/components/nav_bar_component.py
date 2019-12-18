from .base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class NavBarComponent(BaseComponent):

    nav_bar_page_logo_locator = (By.CSS_SELECTOR, "[alt='PHPTRAVELS | Travel Technology Partner']")
    currency_button_locator = (By.CSS_SELECTOR, ".dropdown-currency")
    currency_dropdown_locator = (By.CSS_SELECTOR, "div[x-placement='bottom-end']")
    currency_element_locator = "//a[.='_TEMPLATE_']"
    languauges_button_locator = (By.ID, "dropdownLangauge")
    languauges_dropdown_locator = (By.CSS_SELECTOR, "div[aria-labelledby='dropdownLangauge']")
    languauges_elements_locator = (By.CSS_SELECTOR, "div[aria-labelledby='dropdownLangauge'] > .dropdown-menu-inner > .dropdown-item")


    def __init__(self, driver):

        super().__init__(driver)
    
    def click_page_logo(self):

        logoElement = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of(self.nav_bar_page_logo_locator)
        )
        logoElement.click()

    def open_currency_dropdown(self):

        currencyDropdownElement = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.currency_button_locator)
        )
        currencyDropdownElement.click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.currency_dropdown_locator)
        )

    def select_currency(self, currency):
        
        currency_element_locator = self.currency_element_locator.replace("_TEMPLATE_", currency)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, currency_element_locator))
        ).click()
    
    def open_langauges_dropdown(self):

        langaugesElement = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.languauges_button_locator),
            "Languages Button is not visible"
        )
        langaugesElement.click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.languauges_dropdown_locator)
        )
    
    def get_available_langauges(self):
        
        return dict([ (langauge_element.text, langauge_element.get_attribute('id')) for langauge_element in self.driver.find_elements(*self.languauges_elements_locator) ])


