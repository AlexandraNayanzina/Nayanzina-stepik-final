from .base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_to_basket_link.click()

    def successful_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), "Successful message is not present"

    def book_title_in_successful_message_is_correct(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        book_title_in_successful_message = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_SUCCESSFUL_MESSAGE)
        assert book_title.text + " has been added to your basket." == book_title_in_successful_message.text, "It seems that was added incorrect book"

    def basket_price_equal_book_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        book_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == book_price.text, "The total summ in the basket is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_MESSAGE), "Success message is NOT disappeared, but should disappear"












