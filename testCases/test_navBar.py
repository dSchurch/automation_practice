import sys, os
sys.path.insert(0, os.path.abspath('..'))
import HtmlTestRunner
from automation_practice.resources.components.nav_bar_component import NavBarComponent
from automation_practice.resources.poms.home_page import HomePage
from base_test import BaseTestCase
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class NavBarTest(BaseTestCase):

    def test_click_logo(self):
        
        navBar = NavBarComponent(self.driver)
        navBar.click_page_logo()
        
        homePage = HomePage(self.driver)
        
        homePage.validate_page()
    
    def test_open_currency_dropdown(self):

        navBar = NavBarComponent(self.driver)
        navBar.open_currency_dropdown()
    
    def test_change_page_currency(self):

        navBar = NavBarComponent(self.driver)
        navBar.open_currency_dropdown()
        navBar.select_currency("USD")
    
    def test_open_languages_dropdown(self):

        navBar = NavBarComponent(self.driver)
        navBar.open_langauges_dropdown()
        print(navBar.get_available_langauges())
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\repos\\automation_practice\\reports'))
    