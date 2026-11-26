def test_sort_prices_asc(category_page):
    category_page.open_page()
    category_page.click_sort_by_dropdown()
    category_page.click_sort_by_price_asc()
    category_page.check_prices_sorted_asc()

def test_switch_to_list_view(category_page):
    category_page.open_page()
    category_page.click_list_view_button()
    category_page.check_list_view_is_active()

def test_open_item_card_from_catalog(category_page, item_page):
    category_page.open_page()
    category_page.click_item_card()
    item_page.item_card_opened()
