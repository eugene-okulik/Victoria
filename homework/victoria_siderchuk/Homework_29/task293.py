from playwright.sync_api import Page, expect


def test_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_class('mt-4 text-danger btn btn-primary', timeout=7000)
    button.click()
