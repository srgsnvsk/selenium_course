from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import math
# import time

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        # time.sleep(5)

    # def should_be_success_message(self):
    #     assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"

    # def should_be_correct_product_name(self):
    #     product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    #     success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
    #     assert product_name in success_message, "Product name is not in the success message"

    # def should_be_correct_product_price(self):
    #     product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    #     basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
    #     assert product_price == basket_total, "Product price is not equal to basket total"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except :
            print("No second alert presented")
        # time.sleep(5)