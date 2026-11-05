from playwright.sync_api import Page


def test_student_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Ann')
    page.get_by_placeholder('Last Name').fill('Stevenson')
    page.get_by_placeholder('name@example.com').fill('astv@test.test')
    page.get_by_role('radio', name='Female').click()
    page.get_by_placeholder('Mobile Number').fill('0123456789')
    page.locator('//*[@id="dateOfBirthInput"]').click()
    page.locator('.react-datepicker__month-select').select_option(value="5")
    page.locator('.react-datepicker__year-select').select_option(value="2000")
    page.get_by_role('gridcell', name='10').click()
    subjects_input = page.locator('#subjectsInput')
    subjects_input.fill('Arts')
    subjects_input.press('Enter')
    page.locator('//*[@id="hobbies-checkbox-2"]').click()
    page.get_by_placeholder('Current Address').fill('Paris, Avenue 114a')
    page.locator('#state').click()
    page.get_by_text('Uttar Pradesh').click()
    page.locator('#city').click()
    page.get_by_text('Agra').click()
    page.locator('#submit').click()
