def test_breadcrumbs_text(item_page):
    item_page.open_page()
    item_page.check_breadcrumbs_text()

def test_check_quantity_cannot_be_less_than_one(item_page):
    item_page.open_page()
    item_page.click_minus_button()
    item_page.check_quantity('1')

def test_check_quantity_increases_on_plus_click(item_page):
    item_page.open_page()
    item_page.click_plus_button()
    item_page.check_quantity('2')
