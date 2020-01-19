import time
import pytest
from .Pages.product_page import ProductPage
from .Pages.basket_page import BasketPage
from .Pages.login_page import LoginPage


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        email = str(time.time()) + "@fakemail.org"
        password = "stepikonelove"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.add_to_basket_logined()
        page.should_be_correct_name()
        page.should_be_correct_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()


@pytest.mark.parametrize('link', [pytest.param(0, marks=pytest.mark.xfail),
                         pytest.param(1, marks=pytest.mark.xfail),
                         pytest.param(2, marks=pytest.mark.xfail),
                         pytest.param(3, marks=pytest.mark.xfail),
                         pytest.param(4, marks=pytest.mark.xfail),
                         pytest.param(5, marks=pytest.mark.xfail),
                         pytest.param(6, marks=pytest.mark.xfail),
                         pytest.param(7, marks=pytest.mark.xfail),
                         pytest.param(8, marks=pytest.mark.xfail),
                         pytest.param(9, marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_guest_cant_see_success_message(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [pytest.param(0, marks=pytest.mark.xfail),
                         pytest.param(1, marks=pytest.mark.xfail),
                         pytest.param(2, marks=pytest.mark.xfail),
                         pytest.param(3, marks=pytest.mark.xfail),
                         pytest.param(4, marks=pytest.mark.xfail),
                         pytest.param(5, marks=pytest.mark.xfail),
                         pytest.param(6, marks=pytest.mark.xfail),
                         pytest.param(7, marks=pytest.mark.xfail),
                         pytest.param(8, marks=pytest.mark.xfail),
                         pytest.param(9, marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
