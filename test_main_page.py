import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        time.sleep(4)
        page.go_to_login_page()
        login_link = browser.find_element_by_css_selector("#login_link")
        login_link.click()
        login_page = LoginPage(browser, browser.current_url)
        time.sleep(4)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        time.sleep(4)
        page.should_be_login_link()

def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    alert = self.browser.switch_to.alert
    alert.accept()
    # return LoginPage(browser=self.browser, url=self.browser.current_url)

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.empty_basket_message()
    page.empty_basket_state()
    time.sleep(2)