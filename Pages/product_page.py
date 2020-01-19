from .Base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_basket_button()
        self.add_to_basket()
        self.should_be_correct_name()
        self.should_be_correct_price()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Add to basket link is not presented"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def add_to_basket_logined(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def should_be_correct_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_BASKET_NAME).text
        assert book_name == book_basket_name, \
            f"The book name is not correct: '{book_basket_name}' instead of '{book_name}"

    def should_be_correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price == basket_price, \
            f"The price is not correct: '{price}' instead of '{basket_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
