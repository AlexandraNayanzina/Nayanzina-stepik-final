from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from pages.locators import MainPageLocators, BasePageLocators

class MainPage(BasePage):
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)

    def empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "Basket is NOT empty"

    def empty_basket_state(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "There is NO items in the Basket"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()


