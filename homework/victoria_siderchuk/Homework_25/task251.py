from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_text_input(driver):
    input_data = 'August-22'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_field = driver.find_element(By.ID, 'id_text_string')
    text_field.send_keys(input_data)
    text_field.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data
    print(result_text.text)
