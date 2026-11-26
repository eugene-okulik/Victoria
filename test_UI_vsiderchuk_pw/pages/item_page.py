from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import item_locators as loc


class Item(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def click_add_to_cart_button(self):
        self.find(loc.add_to_cart_loc).click()

    def item_card_opened(self):
        desk_title = self.find(loc.item_title_loc)
        expect(desk_title).to_have_text('Customizable Desk')

    def check_breadcrumbs_text(self):
        breadcrumbs = self.find(loc.item_breadcrumbs_loc)
        expect(breadcrumbs).to_contain_text('All Products')
        expect(breadcrumbs).to_contain_text('Multimedia')
        expect(breadcrumbs).to_contain_text('Office Design Software')

    def click_minus_button(self):
        self.find(loc.minus_button_loc).click()

    def click_plus_button(self):
        self.find(loc.plus_button_loc).click()

    def check_quantity(self, expected_quantity):
        quantity_input = self.find(loc.quantity_input_loc)
        expect(quantity_input).to_have_value(expected_quantity)
