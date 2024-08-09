from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, "#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a > i")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER = (By.CSS_SELECTOR, "#register_form > button")
    SUCCESS_REGISTER_MESSAGE = (By.CSS_SELECTOR, "#messages > div")

class BasketPageLocators():
    BASKET_URL = (By.CSS_SELECTOR, "a[href='/ru/basket/']")
    EMPTY_BASKET = (By.CSS_SELECTOR, "p a[href='/ru/']")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    # PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    # BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
