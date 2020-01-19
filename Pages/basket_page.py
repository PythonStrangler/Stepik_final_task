from .Base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.basket_summary()
        self.basket_should_be_empty()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Url is not correct"

    def basket_summary(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), "There is something in basket " \
                                                                                "already. Basket should be empty."

    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MSG), "There is no empty basket message." \
                                                                            " There might be something in the basket."
