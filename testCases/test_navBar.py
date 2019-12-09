import sys, os
sys.path.insert(0, os.path.abspath('..'))

from automation_practice.resources.components.nav_bar_component import NavBarComponent
from .base_test import BaseTestCase
import unittest

class NavBarTest(BaseTestCase):

    def test_click_logo(self):
        
        navBar = NavBarComponent(self.driver)
        navBar.click_page_logo()
