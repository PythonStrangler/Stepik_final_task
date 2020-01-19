from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CLASS_NAME, "btn-group>a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_MAIL = (By.ID, "id_registration-email")
    REGISTER_PSW1 = (By.ID, "id_registration-password1")
    REGISTER_PSW2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    REGISTER_MESSAGE = (By.CLASS_NAME, "alert.alert-success")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    BOOK_NAME = (By.TAG_NAME, "h1")
    BOOK_BASKET_NAME = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner  strong")
    PRICE = (By.CLASS_NAME, "col-sm-6.product_main .price_color")
    PRICE_BASKET = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner  strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner ")


class BasketPageLocators:
    BASKET_CONTENT = (By.CLASS_NAME, "basket_summary")
    BASKET_IS_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner p")
