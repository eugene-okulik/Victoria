import pytest
from pages.cart_page import Cart
from pages.item_page import Item
from pages.category_page import Category


@pytest.fixture()
def cart_page(page):
    return Cart(page)

@pytest.fixture()
def item_page(page):
    return Item(page)

@pytest.fixture()
def category_page(page):
    return Category(page)
