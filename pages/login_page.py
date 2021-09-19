from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in str(url), "The <login> is NOT in the URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK_NEW), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        register_link = self.browser.find_element(*LoginPageLocators.REGISTER_LINK)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password.send_keys(password)
        register_link.click()

    def open_list_of_books(self):
        book_link_in_menu = self.browser.find_element(*LoginPageLocators.BOOK_LINK_IN_MENU)
        book_link_in_menu.click()

    def open_book_page(self):
        book_link = self.browser.find_element(*LoginPageLocators.BOOK_LINK)
        book_link.click()

