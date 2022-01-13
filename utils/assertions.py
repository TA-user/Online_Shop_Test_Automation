import allure
from assertpy import assert_that

from utils.browser_helper import ElementInteractions
from utils.logging import Logger


class Assertions(ElementInteractions):
    """
    Object instance of Assertions class should initialize in BasePage class. And it would be used by perforce.
    Example usage:
    assertions.element_should_be_clickable(MainPageLocators.ADD_ITEM)
    assertions.element_should_contain_text(MainPageHeaderLocators.USER_MENU, 'user')
    """
    
    Logger.set_logger(Logger())

    @allure.step('Verification of visibility "{1}" element')
    def element_should_be_visible(self, locator):
        element_visibility = self.is_element_visible(locator)
        assert_that(element_visibility, description=f'Required element {locator} is not visible').is_true()

    @allure.step('Verification clickability "{1}" element')
    def element_should_be_clickable(self, locator):
        element_clickability = self.is_element_clickable(locator)
        assert_that(element_clickability, description=f'Required element {locator} is not clickable').is_true()

    @allure.step('Verification that text of element "{1}" contain phrase - "{2}"')
    def element_should_contain_phrase(self, locator, phrase):
        required_element = self.find_element(locator)
        assert_that(required_element.text, description="Element don't contain required phrase").contains(phrase)

    @allure.step('Verification that text of element "{1}" is in phrase "{1}"')
    def element_text_should_be_in_phrase(self, locator, phrase):
        required_element = self.find_element(locator)
        assert_that(phrase, description="Given phrase doesn't contain text of element").contains(required_element.text)
