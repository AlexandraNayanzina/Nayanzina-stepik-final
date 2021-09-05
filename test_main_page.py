import time
from pages.main_page import MainPage

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # browser.get(link)
    # go_to_login_page(browser)

    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    time.sleep(5)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()