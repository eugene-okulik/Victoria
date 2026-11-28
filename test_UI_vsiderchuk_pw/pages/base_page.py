from playwright.sync_api import Page, Locator, expect
from pages.locators import base_locators as loc


class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this page class')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def click_top_cart_button(self):
        top_cart_button = self.find(loc.top_cart_loc)
        expect(self.find(loc.cart_count_loc)).to_have_text("1")
        top_cart_button.click()
