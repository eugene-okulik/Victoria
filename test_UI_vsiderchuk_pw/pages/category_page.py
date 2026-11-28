from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import category_locators as loc


class Category(BasePage):
    page_url = '/shop/category/desks-1'

    def click_sort_by_dropdown(self):
        self.find(loc.sort_by_dropdown_loc).click()

    def click_sort_by_price_asc(self):
        self.find(loc.sort_by_price_asc_loc).click()

    def check_prices_sorted_asc(self):
        all_prices = self.find(loc.item_price_loc).all_inner_texts()
        prices_list = []
        for price in all_prices:
            prices_list.append(float(price.replace(',', '')))
        assert prices_list == sorted(prices_list)

    def click_list_view_button(self):
        self.find(loc.list_view_button_loc).click()

    def check_list_view_is_active(self):
        expect(self.find(loc.active_list_view_button_loc)).to_be_visible()

    def click_item_card(self):
        self.find(loc.customizable_desk_card).click()
