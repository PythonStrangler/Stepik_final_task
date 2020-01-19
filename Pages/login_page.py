from .Base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        login_box = self.browser.find_element(*LoginPageLocators.REGISTER_MAIL)
        login_box.send_keys(email)
        password_box1 = self.browser.find_element(*LoginPageLocators.REGISTER_PSW1)
        password_box1.send_keys(password)
        password_box2 = self.browser.find_element(*LoginPageLocators.REGISTER_PSW2)
        password_box2.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        login_button.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_MESSAGE), "Registration failed"
