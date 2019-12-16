from abc import abstractmethod, ABCMeta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage(metaclass=ABCMeta):

    loading_animation_locator = ".linear-activity"

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def validate_page(self):
        return
    
    def wait_until_page_is_not_loading(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element((By.CSS_SELECTOR, self.loading_animation_locator))
        )

class InvalidPageExpection(Exception):
    pass