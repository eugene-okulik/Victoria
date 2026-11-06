from playwright.sync_api import Page


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username_input = page.get_by_role('textbox', name='username')
    username_input.fill('john_qa')
    password_input = page.get_by_role('textbox', name='password')
    password_input.fill('qwerty123')
    login_button = page.get_by_role('button')
    login_button.click()
