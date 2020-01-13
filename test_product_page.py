import pytest
from .Pages.product_page import ProductPage


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.should_be_product_page()  # выполняем метод страницы - добавляем в корзину, вводим роверочный код


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
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_guest_cant_see_success_message(browser, link):
    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
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
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()


# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    # 1.Гость открывает страницу товара
    # 2.Переходит в корзину по кнопке в шапке
    # 3.Ожидаем, что в корзине нет товаров
    # 4.Ожидаем, что есть текст о том что корзина пуста
    # todo чет надо а че хз

    # pytest -v -s --tb=line --language=en test_product_page.py::test_message_disappeared_after_adding_product_to_basket
