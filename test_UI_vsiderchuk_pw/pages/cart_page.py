from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import cart_locators as loc
from pages.locators import base_locators as base_loc


class Cart(BasePage):
    page_url = '/shop/cart'

    def check_empty_cart_text(self, expected_text):
        empty_cart_alert = self.find(loc.empty_cart_text_loc)
        expect(empty_cart_alert).to_have_text(expected_text)

    def check_item_name_in_cart(self, expected_name):
        item_name = self.find(loc.item_name_loc)
        expect(item_name).to_have_text(expected_name)

    def click_plus_button(self):
        self.find(loc.plus_one_item_loc).click()

    def check_item_price_doubles(self):
        old_price_text = self.find(loc.item_price_loc).inner_text()
        old_price = float(old_price_text)
        self.click_plus_button()
        expect(self.find(base_loc.cart_count_loc)).to_have_text("2")
        new_price_text = self.find(loc.item_price_loc).inner_text()
        new_price = float(new_price_text)
        assert new_price == old_price * 2
