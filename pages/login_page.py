from .base_page import BasePage
from .locators import LoginPageLocators
import faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        print(email)
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        password = f.password()
        print(password)
        input_password = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        input_password.send_keys(password)
        input_repeat_password = self.browser.find_element(*LoginPageLocators.INPUT_REPEAT_PASSWORD)
        input_repeat_password.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER)
        register.click()

    def should_be_register_message(self):
        register_message = self.browser.find_element(*LoginPageLocators.SUCCESS_REGISTER_MESSAGE).text

        print(register_message)

        assert register_message in register_message, \
            f"Expected 'Спасибо за регистрацию!', but got {register_message}"
