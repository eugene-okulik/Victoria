def test_empty_cart_text(cart_page):
    cart_page.open_page()
    cart_page.check_empty_cart_text('Your cart is empty!')

def test_add_item_to_cart(cart_page, item_page):
    item_page.open_page()
    item_page.click_add_to_cart_button()
    item_page.click_top_cart_button()
    cart_page.check_item_name_in_cart('Office Design Software')

def test_price_doubles_after_increasing_item(cart_page, item_page):
    item_page.open_page()
    item_page.click_add_to_cart_button()
    item_page.click_top_cart_button()
    cart_page.check_item_price_doubles()
