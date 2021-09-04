import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button is not None, "There is NO 'Add to Basket' button"

