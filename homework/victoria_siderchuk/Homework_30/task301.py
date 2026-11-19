from playwright.sync_api import Page, expect, Route
import re
import json


def test_iphone(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][1]['familyTypes'][0]['productName'] = 'яблокофон 18 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile('/step0_iphone/'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('[data-trigger-id="digitalmat-2"]').click()
    popup_title = page.locator('[data-autom="DigitalMat-overlay-header-1-0"]')
    expect(popup_title).to_have_text('яблокофон 18 про')
