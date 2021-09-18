from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK_NEW = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTER_LINK = (By.CSS_SELECTOR, "#register_form > button")
    REG_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div")
    BOOK_LINK_IN_MENU = (By.CSS_SELECTOR, "#browse > li > ul > li.dropdown-submenu > a")
    BOOK_LINK = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div > section > div > ol > li:nth-child(2)")

class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BOOK_TITLE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_TITLE_IN_SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "# basket_formset > div")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


