from playwright.sync_api import Page, expect, Dialog


def test_alert(page: Page):

    def ok_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', ok_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    result = page.locator('#result-text')
    expect(result).to_have_text('Ok')
