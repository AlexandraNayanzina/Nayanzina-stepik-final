from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from pages.locators import MainPageLocators, ProductPageLocators, BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "Basket is NOT empty"

    def empty_basket_state(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "There is NO items in the Basket"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

