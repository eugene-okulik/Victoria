from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_student_registration(driver):
    first_name_data = "Jane"
    last_name_data = "Ostin"
    email_data = "ostin@test.com"
    mobile_number_data = "1234567890"
    subject_data_1 = "Maths"
    subject_data_2 = "Arts"
    current_address_data = "Spring avenue, 135"
    driver.get("https://demoqa.com/automation-practice-form")
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys(first_name_data)
    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys(last_name_data)
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys(email_data)
    gender = driver.find_element(By.CSS_SELECTOR, '[value="Female"]')
    gender.click()
    mobile_number = driver.find_element(By.ID, 'userNumber')
    mobile_number.send_keys(mobile_number_data)
    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()
    month_selector = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    month_selector.click()
    month_data = Select(month_selector)
    month_data.select_by_value('0')
    year_selector = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    year_selector.click()
    year_data = Select(year_selector)
    year_data.select_by_value('1990')
    day_data = driver.find_element(By.CSS_SELECTOR, '[aria-label="Choose Friday, January 5th, 1990"]')
    day_data.click()
    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.click()
    subjects_input.send_keys(subject_data_1)
    subjects_selector = driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__option')
    subjects_selector.click()
    subjects_input.send_keys(subject_data_2)
    subjects_selector = driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__option')
    subjects_selector.click()
    hobbies = driver.find_element(By.ID, 'hobbies-checkbox-1')
    hobbies.click()
    current_address = driver.find_element(By.ID, 'currentAddress')
    current_address.send_keys(current_address_data)
    state = driver.find_element(By.ID, 'react-select-3-input')
    state.click()
    state_data = driver.find_element(By.ID, 'react-select-3-option-0')
    state_data.click()
    city = driver.find_element(By.ID, 'react-select-4-input')
    city.click()
    city_data = driver.find_element(By.ID, 'react-select-4-option-0')
    city_data.click()
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()
    submit_result = driver.find_element(By.CLASS_NAME, 'modal-body')
    print(submit_result.text)
